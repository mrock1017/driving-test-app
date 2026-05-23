from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session
)

from utils.questions import load_questions

from languages.ui import get_ui

import random
import time
import stripe
import os
from models import (
    User,
    ScoreHistory,
    db
)

tests = Blueprint(
    'tests',
    __name__
)

stripe.api_key = os.getenv(
    "STRIPE_SECRET_KEY"
)


# =========================================================
# ✅ MENU
# =========================================================

@tests.route('/')
@tests.route('/menu')
def menu():

    if 'lang' not in session:

        session['lang'] = 'en'

    return render_template(

        'menu.html',

        ui=get_ui()
    )

# =========================================================
# 🌐 SET LANGUAGE
# =========================================================

@tests.route('/set-language/<lang>')
def set_language(lang):

    allowed_languages = [

        'en',
        'tl',
        'ne',
        'vi',
        'pt'
    ]

    if lang in allowed_languages:

        session['lang'] = lang

    return redirect('/menu')

# =========================================================
# ✅ NEXT QUESTION ROUTE
# FIXES SKIPPED QUESTIONS
# =========================================================

@tests.route('/next')
def next_question():

    if 'current' in session:

        session['current'] += 1

    return redirect('/question')

# =========================================================
# 🚀 START MODE
# =========================================================

@tests.route('/start/<mode>/<test>')
def start_mode(mode, test):

    # =====================================================
    # 🧹 CLEAR OLD SESSION
    # =====================================================

    session.pop('order', None)
    session.pop('answers', None)
    session.pop('current', None)

    language = session.get('lang', 'en')

    is_premium = session.get(
        'is_premium',
        False
    )

    # =====================================================
    # 🔒 PREMIUM PROTECTION
    # =====================================================

    if mode == "honmen":

        # =================================================
        # 👤 GUEST USERS
        # =================================================

        if 'user_id' not in session:

            return redirect('/register')

        # =================================================
        # 🔒 FREE USERS
        # =================================================

        if not is_premium:

            return redirect('/upgrade')

    # =====================================================
    # 👤 GUEST USERS
    # =====================================================

    if 'user_id' not in session:

        # guests can ONLY access reviewer

        if "reviewer" not in mode:

            return redirect('/register')

    # =====================================================
    # 🔒 FREE USERS
    # =====================================================

    elif not is_premium:

        if mode == "karimen":

            if test != "karimen_1":

                return redirect('/upgrade')

    # =====================================================
    # 📂 FOLDER
    # =====================================================

    if mode == "karimen":

        folder = "karimen"

    elif mode == "honmen":

        folder = "honmen"

    elif mode == "reviewer_karimen":

        folder = "reviewer/karimen"

    elif mode == "reviewer_honmen":

        folder = "reviewer/honmen"

    else:

        return "Invalid mode"

    # =====================================================
    # ✅ LOAD QUESTIONS
    # =====================================================

    questions = load_questions(

        folder,

        language,

        f"{test}.json"
    )

    if len(questions) == 0:

        return "No questions found."

    # =====================================================
    # 💾 SAVE SESSION
    # =====================================================

    session['folder'] = folder
    session['questions_file'] = test
    session['answers'] = []
    session['current'] = 0
    session['mode'] = mode

    # =====================================================
    # 🏁 HONMEN MODE
    # =====================================================

    if mode == "honmen":

        normal_questions = []
        grouped_questions = []

        for i, q in enumerate(questions):

            if "items" in q:

                grouped_questions.append(i)

            else:

                normal_questions.append(i)

        selected_normal = random.sample(

            normal_questions,

            min(90, len(normal_questions))
        )

        selected_grouped = random.sample(

            grouped_questions,

            min(5, len(grouped_questions))
        )

        order = (
            selected_normal
            +
            selected_grouped
        )

        session['duration'] = 50 * 60

    # =====================================================
    # 🧠 REVIEWER MODE
    # =====================================================

    elif "reviewer" in mode:

                # =================================================
        # 🚫 GUEST REVIEWER LIMIT
        # =================================================

        if 'user_id' not in session:

            if session.get('guest_reviewer_done'):

                return redirect('/register')

        # =================================================
        # 🚫 FREE ACCOUNT REVIEWER LIMIT
        # =================================================

        elif not is_premium:

            existing_attempt = (

                ScoreHistory.query

                .filter_by(
                    user_id=session['user_id'],
                    mode=mode
                )

                .first()
            )

            if existing_attempt:

                return redirect('/upgrade')

        reviewer_indexes = []

        # ✅ ONLY NORMAL QUESTIONS

        for i, q in enumerate(questions):

            if "items" not in q:

                reviewer_indexes.append(i)

        random.shuffle(reviewer_indexes)

        # =================================================
        # 👤 GUEST USERS = 10 QUESTIONS
        # =================================================

        if 'user_id' not in session:

            order = reviewer_indexes[:20]

        # =================================================
        # 🔒 FREE USERS = 20 QUESTIONS
        # =================================================

        elif not is_premium:

            order = reviewer_indexes[:20]

        # =================================================
        # ✅ PREMIUM USERS = UNLIMITED
        # =================================================

        else:

            order = reviewer_indexes

        # =================================================
        # ✅ REVIEWER HAS NO TIMER
        # =================================================

        session['duration'] = None

    # =====================================================
    # 📝 MOCK TEST MODES
    # =====================================================

    else:

        total_questions = 50

        if len(questions) > total_questions:

            order = random.sample(

                range(len(questions)),

                total_questions
            )

        else:

            order = list(
                range(len(questions))
            )

            random.shuffle(order)

        session['duration'] = 30 * 60

    # =====================================================
    # ⏱ SESSION
    # =====================================================

    session['order'] = order

    session['start_time'] = int(time.time())

    return redirect('/question')

# =========================================================
# ❓ QUESTION PAGE
# =========================================================

@tests.route('/question', methods=['GET', 'POST'])
def question():

    if 'order' not in session:

        return redirect('/menu')

    language = session.get('lang', 'en')

    questions = load_questions(

        session['folder'],

        language,

        f"{session['questions_file']}.json"
    )

    order = session['order']

    current = session.get('current', 0)

    # =====================================================
    # 🏁 FINISHED
    # =====================================================

    if current >= len(order):

        # =================================================
        # 👤 GUEST REVIEWER RESULT
        # =================================================

        if (

            'user_id' not in session

            and

            "reviewer" in session['mode']

        ):

            answers = session.get('answers', [])

            score = 0

            for i in range(min(len(answers), len(order))):

                q = questions[order[i]]

                correct_answer = (
                    q['answer']
                    .strip()
                    .lower()
                )

                user_answer = (
                    (answers[i] or '')
                    .strip()
                    .lower()
                )

                if user_answer == correct_answer:

                    score += 1

            session['guest_reviewer_done'] = True

            return render_template(

                'guest_result.html',

                score=score,

                total=len(order)
            )

                # =================================================
        # 🔒 FREE REVIEWER LIMIT
        # =================================================

        if (

            'user_id' in session

            and

            not session.get('is_premium')

            and

            "reviewer" in session['mode']

        ):

            answers = session.get('answers', [])

            score = 0

            for i in range(min(len(answers), len(order))):

                q = questions[order[i]]

                correct_answer = (
                    q['answer']
                    .strip()
                    .lower()
                )

                user_answer = (
                    (answers[i] or '')
                    .strip()
                    .lower()
                )

                if user_answer == correct_answer:

                    score += 1

            # =============================================
            # 💾 SAVE HISTORY
            # =============================================

            history = ScoreHistory(

                user_id=session['user_id'],

                mode=session['mode'],

                score=score,

                total=len(order),

                passed=False
            )

            db.session.add(history)

            db.session.commit()

            return redirect('/upgrade')

    # =====================================================
    # 📦 CURRENT QUESTION
    # =====================================================

    q = questions[order[current]]

    # =====================================================
    # ⏱ TIMER
    # =====================================================

    remaining_time = None

    if session.get('duration'):

        elapsed = int(time.time()) - session['start_time']

        remaining_time = max(

            0,

            session['duration'] - elapsed
        )

    # =====================================================
    # 📝 SAVE ANSWER
    # =====================================================

    if request.method == 'POST':

        # =================================================
        # 🧠 REVIEWER MODE
        # =================================================

        if "reviewer" in session['mode']:

            answer = request.form.get('answer')

            correct_answer = q['answer']

            is_correct = (

                (answer or '').strip().lower()

                ==

                correct_answer.strip().lower()
            )

            # =================================================
            # ✅ SAFE ANSWER SAVE
            # =================================================

            answers = session.get('answers', [])

            if len(answers) <= current:

                answers.append(answer)

            else:

                answers[current] = answer

            session['answers'] = answers

            # =================================================
            # ❌ DO NOT INCREMENT HERE
            # =================================================

            return render_template(

                'question.html',

                q=q,

                index=current + 1,

                display_index=current + 1,

                total=len(order),

                remaining=remaining_time,

                is_reviewer=True,

                feedback=True,

                is_correct=is_correct,

                user_answer=answer,

                correct_answer=correct_answer,

                explanation=q.get(
                    'explanation',
                    ''
                ),

                ai_explanation=q.get(
                    'ai_explanation',
                    ''
                ),

                mode=session['mode'],

                ui=get_ui()
            )

        # =================================================
        # 📝 GROUP QUESTIONS
        # =================================================

        if "items" in q:

            group_answers = []

            for item in q['items']:

                ans = request.form.get(

                    f"answer_{item['number']}"
                )

                group_answers.append(ans)

            # =================================================
            # ✅ SAFE SAVE
            # =================================================

            answers = session.get('answers', [])

            if len(answers) <= current:

                answers.append(group_answers)

            else:

                answers[current] = group_answers

            session['answers'] = answers

        # =================================================
        # 📝 NORMAL QUESTIONS
        # =================================================

        else:

            answer = request.form.get('answer')

            # =================================================
            # ✅ SAFE SAVE
            # =================================================

            answers = session.get('answers', [])

            if len(answers) <= current:

                answers.append(answer)

            else:

                answers[current] = answer

            session['answers'] = answers

        # =================================================
        # ✅ NORMAL MODES INCREMENT HERE
        # =================================================

        session['current'] = current + 1

        return redirect('/question')

    # =====================================================
    # 🎨 RENDER
    # =====================================================

    return render_template(

        'question.html',

        q=q,

        index=current + 1,

        display_index=current + 1,

        total=len(order),

        remaining=remaining_time,

        is_reviewer="reviewer" in session['mode'],

        mode=session['mode'],

        ui=get_ui()
    )

# =========================================================
# 🏆 RESULT PAGE
# =========================================================

@tests.route('/result')
def result():

    if 'mode' not in session:

        return redirect('/menu')

    if "reviewer" in session['mode']:

        return redirect('/menu')

    language = session.get('lang', 'en')

    questions = load_questions(

        session['folder'],

        language,

        f"{session['questions_file']}.json"
    )

    order = session.get('order', [])

    answers = session.get('answers', [])

    results = []

    score = 0

    total_questions = 0

    for i, idx in enumerate(order):

        q = questions[idx]

        # =================================================
        # 🧠 GROUP QUESTIONS
        # =================================================

        if 'items' in q:

            if i >= len(answers):

                continue

            user_group_answers = answers[i]

            for j, item in enumerate(q['items']):

                total_questions += 1

                user_answer = None

                if j < len(user_group_answers):

                    user_answer = (
                        user_group_answers[j]
                    )

                correct = (

                    (user_answer or '')
                    .strip()
                    .lower()

                    ==

                    item['answer']
                    .strip()
                    .lower()
                )

                if correct:

                    score += 1

                results.append({

                    "question":
                    item['question'],

                    "your_answer":
                    user_answer,

                    "correct_answer":
                    item['answer'],

                    "explanation":
                    item.get(
                        'explanation',
                        ''
                    ),

                    "is_correct":
                    correct,

                    "image":
                    q.get("image")
                })

        # =================================================
        # 📝 NORMAL QUESTIONS
        # =================================================

        else:

            total_questions += 1

            user_answer = None

            if i < len(answers):

                user_answer = answers[i]

            correct = (

                (user_answer or '')
                .strip()
                .lower()

                ==

                q['answer']
                .strip()
                .lower()
            )

            if correct:

                score += 1

            results.append({

                "question":
                q['question'],

                "your_answer":
                user_answer,

                "correct_answer":
                q['answer'],

                "explanation":
                q['explanation'],

                "is_correct":
                correct,

                "image":
                q.get("image")
            })

    session['last_score'] = score

    session['last_total'] = total_questions

    passing_score = int(
        total_questions * 0.9
    )

    if session['mode'] == "honmen":

        passing_score = 90

    passed = score >= passing_score

    # =====================================================
    # 💾 SAVE HISTORY
    # =====================================================

    if 'user_id' in session:

        history = ScoreHistory(

            user_id=session['user_id'],

            mode=session['mode'],

            score=score,

            total=total_questions,

            passed=passed
        )

        db.session.add(history)

        db.session.commit()

    return render_template(

        'result.html',

        score=score,

        total=total_questions,

        results=results,

        passed=passed,

        passing_score=passing_score,

        ui=get_ui()
    )

# =========================================================
# 📊 SCORE HISTORY PAGE
# =========================================================

@tests.route('/score-history')
def score_history():

    if 'user_id' not in session:

        return redirect('/login')

    history = (

        ScoreHistory.query

        .filter_by(
            user_id=session['user_id']
        )

        .order_by(
            ScoreHistory.id.desc()
        )

        .all()
    )

    return render_template(

        'score_history.html',

        history=history,

        ui=get_ui()
    )

# =========================================================
# 💳 STRIPE CHECKOUT
# =========================================================

@tests.route('/create-checkout-session/<plan>')
def create_checkout_session(plan):

    # =====================================================
    # 👤 LOGIN REQUIRED
    # =====================================================

    if 'user_id' not in session:

        return redirect('/register')

    # =====================================================
    # 💳 SELECT PRICE ID
    # =====================================================

    if plan == "yearly":

        price_id = os.getenv(
            "STRIPE_YEARLY_PRICE_ID"
        )

    else:

        price_id = os.getenv(
            "STRIPE_MONTHLY_PRICE_ID"
        )

    # =====================================================
    # 🚀 CREATE STRIPE SESSION
    # =====================================================

    checkout_session = stripe.checkout.Session.create(

        payment_method_types=['card'],

        mode='subscription',

        line_items=[{

            'price': price_id,

            'quantity': 1,
        }],

        success_url=request.host_url +
        'payment-success',

        cancel_url=request.host_url +
        'upgrade',
    )

    return redirect(

        checkout_session.url,

        code=303
    )

# =========================================================
# ✅ PAYMENT SUCCESS
# =========================================================

@tests.route('/payment-success')
def payment_success():

    if 'user_id' not in session:

        return redirect('/login')

    user = User.query.get(
        session['user_id']
    )

    if user:

        user.is_premium = True

        db.session.commit()

        session['is_premium'] = True

    return render_template(
        'payment_success.html'
    )