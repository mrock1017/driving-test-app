from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session
)

from utils.questions import load_questions

from languages.ui import get_ui

import os
import json
import random
import time

from models import (
    User,
    ScoreHistory,
    db
)

tests = Blueprint(
    'tests',
    __name__
)

@tests.route('/test-page')
def test_page():

    return """
    <h1>
    ✅ Tests Blueprint Works
    </h1>
    """
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
# 🚀 START MODE
# =========================================================

@tests.route('/start/<mode>/<test>')
def start_mode(mode, test):

    language = session.get('lang', 'en')

    is_premium = session.get(
        'is_premium',
        False
    )

    # =====================================================
    # 🔒 PREMIUM PROTECTION
    # =====================================================

    # Honmen = Premium Only

    if mode == "honmen":

        if not is_premium:

            return redirect('/upgrade')

    # Free users can only access Karimen Test 1

    if not is_premium:

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

    # =====================================================
    # 🔒 GUEST SAMPLE MODE
    # =====================================================

    # Guests only get 10 random questions

    if 'user_id' not in session:

        questions = random.sample(

            questions,

            min(10, len(questions))
        )

    # =====================================================
    # 🔒 FREE REVIEWER LIMIT
    # =====================================================

    # Free accounts only get 20 reviewer questions

    elif not is_premium:

        if "reviewer" in mode:

            questions = questions[:20]

    # =====================================================
    # ❌ NO QUESTIONS
    # =====================================================

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
    # 📝 OTHER MODES
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

        # Reviewer = No timer

        if "reviewer" in mode:

            session['duration'] = None

        else:

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
    # 🏁 TEST FINISHED
    # =====================================================

    if current >= len(order):
            # 👤 GUEST USERS

        if 'user_id' not in session:

            answers = session.get('answers', [])

            score = 0

            for i, answer in enumerate(answers):

                q = questions[order[i]]

                correct_answer = (
                    q['answer']
                    .strip()
                    .lower()
                )

                user_answer = (
                    (answer or '')
                    .strip()
                    .lower()
                )

                if user_answer == correct_answer:

                    score += 1

            return render_template(

                'guest_result.html',

                score=score,

                total=len(order)
            )
        
        return redirect('/result')

    # =====================================================
    # 📦 CURRENT QUESTION
    # =====================================================

    q = questions[order[current]]

    # =====================================================
    # 📝 SAVE ANSWER
    # =====================================================

    if request.method == 'POST':

        answer = request.form.get('answer')

        answers = session.get('answers', [])

        answers.append(answer)

        session['answers'] = answers

        session['current'] = current + 1

        return redirect('/question')

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
    # 🎨 RENDER
    # =====================================================

    return render_template(

        'question.html',

        q=q,

        index=current + 1,

        total=len(order),

        remaining_time=remaining_time,

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

        # 🔒 GUEST RESULT PAGE

    if 'user_id' not in session:

        return render_template(

            'guest_result.html',

            score=score,

            total=total_questions
        )

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
# 📊 HISTORY
# =========================================================

@tests.route('/history')
def history():

    check = login_required()

    if check:

        return check

    records = ScoreHistory.query.filter_by(

        user_id=session['user_id']

    ).order_by(

        ScoreHistory.created_at.desc()

    ).all()

    return render_template(

        'history.html',

        history=records,

        ui=get_ui()
    )
