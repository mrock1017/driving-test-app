from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

import os
import json
import random
import time

app = Flask(__name__)

# =========================================================
# ✅ SECRET KEY
# =========================================================

app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY',
    'super-secret-key'
)

# =========================================================
# ✅ DATABASE
# =========================================================

app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///users.db'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# =========================================================
# ✅ DEBUG
# =========================================================

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = False


# =========================================================
# 👤 USER MODEL
# =========================================================

class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(300),
        nullable=False
    )

    is_premium = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=db.func.now()
    )


# =========================================================
# 📊 SCORE HISTORY MODEL
# =========================================================

class ScoreHistory(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )

    mode = db.Column(
        db.String(100)
    )

    score = db.Column(
        db.Integer
    )

    total = db.Column(
        db.Integer
    )

    passed = db.Column(
        db.Boolean
    )

    created_at = db.Column(
        db.DateTime,
        default=db.func.now()
    )


# =========================================================
# 🌐 UI TRANSLATIONS
# =========================================================

UI_TEXT = {

    "en": {

        "study_mode": "🧠 Study Mode",
        "reviewer_karimen": "🧠 Reviewer Karimen",
        "reviewer_honmen": "🧠 Reviewer Honmen",

        "karimen_mock": "📝 Karimen Mock Test",
        "karimen_test_1": "📝 Karimen Test 1",
        "karimen_test_2": "📝 Karimen Test 2",

        "honmen_mock": "🏁 Honmen Mock Test",
        "honmen_test_1": "🏁 Honmen Test 1",
        "honmen_test_2": "🏁 Honmen Test 2",
        "honmen_test_3": "🏁 Honmen Test 3",

        "app_info": "⚙️ App Information",
        "score_history": "📊 Score History",
        "privacy": "🔒 Privacy Policy",
        "terms": "📄 Terms of Use",
        "contact": "✉️ Contact Us",

        "dark_mode": "🌙 Dark Mode",

        "login": "👤 Login",
        "register": "📝 Register",
        "logout": "🚪 Logout",
        "welcome": "Welcome",

        "ai_title": "🧠 AI Tutor",

        "premium": "⭐ Premium User"
    },

    "tl": {

        "study_mode": "🧠 Study Mode",
        "reviewer_karimen": "🧠 Reviewer Karimen",
        "reviewer_honmen": "🧠 Reviewer Honmen",

        "karimen_mock": "📝 Karimen Mock Test",
        "karimen_test_1": "📝 Karimen Test 1",
        "karimen_test_2": "📝 Karimen Test 2",

        "honmen_mock": "🏁 Honmen Mock Test",
        "honmen_test_1": "🏁 Honmen Test 1",
        "honmen_test_2": "🏁 Honmen Test 2",
        "honmen_test_3": "🏁 Honmen Test 3",

        "app_info": "⚙️ Impormasyon ng App",
        "score_history": "📊 Kasaysayan ng Score",
        "privacy": "🔒 Patakaran sa Privacy",
        "terms": "📄 Mga Tuntunin ng Paggamit",
        "contact": "✉️ Makipag-ugnayan",

        "dark_mode": "🌙 Dark Mode",

        "login": "👤 Login",
        "register": "📝 Register",
        "logout": "🚪 Logout",
        "welcome": "Welcome",

        "ai_title": "🧠 AI Tutor",

        "premium": "⭐ Premium User"
    },

    "ne": {

        "study_mode": "🧠 अध्ययन मोड",
        "reviewer_karimen": "🧠 Reviewer Karimen",
        "reviewer_honmen": "🧠 Reviewer Honmen",

        "karimen_mock": "📝 Karimen Mock Test",
        "karimen_test_1": "📝 Karimen Test 1",
        "karimen_test_2": "📝 Karimen Test 2",

        "honmen_mock": "🏁 Honmen Mock Test",
        "honmen_test_1": "🏁 Honmen Test 1",
        "honmen_test_2": "🏁 Honmen Test 2",
        "honmen_test_3": "🏁 Honmen Test 3",

        "app_info": "⚙️ एप जानकारी",
        "score_history": "📊 स्कोर इतिहास",
        "privacy": "🔒 गोपनीयता नीति",
        "terms": "📄 प्रयोगका सर्तहरू",
        "contact": "✉️ सम्पर्क गर्नुहोस्",

        "dark_mode": "🌙 Dark Mode",

        "login": "👤 Login",
        "register": "📝 Register",
        "logout": "🚪 Logout",
        "welcome": "Welcome",

        "ai_title": "🧠 AI Tutor",

        "premium": "⭐ Premium User"
    }
}


# =========================================================
# 🌐 GET UI LANGUAGE
# =========================================================

def get_ui():

    language = session.get('lang', 'en')

    return UI_TEXT.get(
        language,
        UI_TEXT['en']
    )


# =========================================================
# 🔐 LOGIN REQUIRED
# =========================================================

def login_required():

    if 'user_id' not in session:

        return redirect('/login')


# =========================================================
# 🤖 AI EXPLANATION
# =========================================================

def generate_ai_explanation(
    question,
    correct_answer,
    user_answer,
    is_correct
):

    if is_correct:

        return (
            "✅ Excellent driving judgment. "
            "You correctly understood the road rule "
            f"and selected the proper answer "
            f"({correct_answer}). "
            "This question tests traffic law awareness, "
            "safe driving behavior, and hazard prediction."
        )

    return (
        f"❌ Your answer was '{user_answer}', "
        f"but the correct answer is "
        f"'{correct_answer}'. "
        "Focus carefully on road signs, "
        "pedestrian safety, and defensive driving."
    )


# =========================================================
# ✅ LOAD QUESTIONS
# =========================================================

def load_questions(folder, language, filename):

    filepath = os.path.join(
        "data",
        folder,
        language,
        filename
    )

    if not os.path.exists(filepath):

        filepath = os.path.join(
            "data",
            folder,
            "en",
            filename
        )

    if not os.path.exists(filepath):

        return []

    try:

        with open(
            filepath,
            encoding='utf-8-sig'
        ) as f:

            return json.load(f)

    except Exception as e:

        print("JSON ERROR:", e)

        return []


# =========================================================
# 🌐 SET LANGUAGE
# =========================================================

@app.route('/set-language/<lang>')
def set_language(lang):

    allowed = ['en', 'tl', 'ne']

    if lang not in allowed:

        lang = 'en'

    session['lang'] = lang

    session.modified = True

    return redirect('/menu')


# =========================================================
# 👤 REGISTER
# =========================================================

@app.route('/register', methods=['GET', 'POST'])
def register():

    ui = get_ui()

    error = None

    if request.method == 'POST':

        username = (
            request.form.get('username')
            .strip()
        )

        email = (
            request.form.get('email')
            .strip()
            .lower()
        )

        password = request.form.get('password')

        existing_email = User.query.filter_by(
            email=email
        ).first()

        if existing_email:

            error = "Email already exists."

        else:

            existing_username = (
                User.query.filter_by(
                    username=username
                ).first()
            )

            if existing_username:

                error = "Username already taken."

            elif len(password) < 6:

                error = (
                    "Password must be at least "
                    "6 characters."
                )

            else:

                hashed = generate_password_hash(
                    password
                )

                new_user = User(

                    username=username,

                    email=email,

                    password=hashed
                )

                db.session.add(new_user)

                db.session.commit()

                return redirect('/login')

    return render_template(

        'register.html',

        error=error,

        ui=ui
    )


# =========================================================
# 👤 LOGIN
# =========================================================

@app.route('/login', methods=['GET', 'POST'])
def login():

    ui = get_ui()

    error = None

    if request.method == 'POST':

        email = (
            request.form.get('email')
            .strip()
            .lower()
        )

        password = request.form.get('password')

        user = User.query.filter_by(
            email=email
        ).first()

        if user and check_password_hash(
            user.password,
            password
        ):

            session['user_id'] = user.id

            session['username'] = user.username

            session['is_premium'] = (
                user.is_premium
            )

            return redirect('/menu')

        else:

            error = (
                "Invalid login credentials."
            )

    return render_template(

        'login.html',

        error=error,

        ui=ui
    )


# =========================================================
# 🚪 LOGOUT
# =========================================================

@app.route('/logout')
def logout():

    session.clear()

    return redirect('/menu')


# =========================================================
# ✅ MENU
# =========================================================

@app.route('/')
@app.route('/menu')
def menu():

    if 'lang' not in session:

        session['lang'] = 'en'

    return render_template(

        'menu.html',

        ui=get_ui()
    )


# =========================================================
# ❌ QUIT EXAM
# =========================================================

@app.route('/quit')
def quit_exam():

    session.pop('mode', None)
    session.pop('answers', None)
    session.pop('current', None)
    session.pop('order', None)
    session.pop('folder', None)
    session.pop('questions_file', None)

    return redirect('/menu')


# =========================================================
# 🚀 START MODE
# =========================================================

@app.route('/start/<mode>/<test>')
def start_mode(mode, test):

    language = session.get('lang', 'en')

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

    questions = load_questions(

        folder,

        language,

        f"{test}.json"
    )

    if len(questions) == 0:

        return "No questions found."

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

        # ✅ KEEP GROUP QUESTIONS AT END

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

        if "reviewer" in mode:

            session['duration'] = None

        else:

            session['duration'] = 30 * 60

    session['order'] = order

    session['start_time'] = int(time.time())

    return redirect('/question')


# =========================================================
# ❓ QUESTION PAGE
# =========================================================

@app.route('/question', methods=['GET', 'POST'])
def question():

    if 'mode' not in session:

        return redirect('/menu')

    language = session.get('lang', 'en')

    questions = load_questions(

        session['folder'],

        language,

        f"{session['questions_file']}.json"
    )

    order = session.get('order', [])

    if len(order) == 0:

        return redirect('/menu')

    if session['current'] >= len(order):

        return redirect('/result')

    idx = order[session['current']]

    q = questions[idx]

    is_reviewer = (
        "reviewer" in session['mode']
    )

    remaining = None

    if not is_reviewer:

        remaining = session['duration'] - (

            int(time.time())

            - session['start_time']
        )

        if remaining <= 0:

            return redirect('/result')

    feedback = False

    correct_answer = None
    explanation = None
    is_correct = None
    user_answer = None
    ai_explanation = None

    if request.method == 'POST':

        if 'items' in q:

            group_answers = []

            for item in q['items']:

                ans = request.form.get(
                    f"answer_{item['number']}"
                )

                group_answers.append(ans)

            answers = session.get(
                'answers',
                []
            )

            answers.append(group_answers)

            session['answers'] = answers

            session['current'] += 1

            session.modified = True

            return redirect('/question')

        answer = request.form.get('answer')

        if answer:

            correct_answer = q['answer']

            explanation = q['explanation']

            user_answer = answer

            is_correct = (

                answer.strip().lower()

                ==

                correct_answer.strip().lower()
            )

            ai_explanation = (
                generate_ai_explanation(

                    q['question'],

                    correct_answer,

                    user_answer,

                    is_correct
                )
            )

            answers = session.get(
                'answers',
                []
            )

            answers.append(answer)

            session['answers'] = answers

            session.modified = True

            if is_reviewer:

                feedback = True

            else:

                session['current'] += 1

                return redirect('/question')

    return render_template(

        'question.html',

        q=q,

        index=session['current'],

        total=len(order),

        remaining=remaining,

        is_reviewer=is_reviewer,

        feedback=feedback,

        correct_answer=correct_answer,

        explanation=explanation,

        is_correct=is_correct,

        user_answer=user_answer,

        ai_explanation=ai_explanation,

        ui=get_ui()
    )


# =========================================================
# ➡ NEXT QUESTION
# =========================================================

@app.route('/next')
def next_question():

    if 'current' in session:

        session['current'] += 1

    return redirect('/question')


# =========================================================
# 🏆 RESULT PAGE
# =========================================================

@app.route('/result')
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
        # 🏁 GROUP QUESTIONS
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

    # =====================================================
    # ✅ PASSING SCORE
    # =====================================================

    passing_score = int(
        total_questions * 0.9
    )

    if session['mode'] == "honmen":

        passing_score = 90

    passed = score >= passing_score

    # =====================================================
    # 📊 DATABASE SCORE HISTORY
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
# 📊 HISTORY
# =========================================================

@app.route('/history')
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

# =========================================================
# 🔒 PRIVACY POLICY
# =========================================================

@app.route('/privacy')
def privacy():

    return render_template(

        'privacy.html',

        ui=get_ui()
    )


# =========================================================
# 📄 TERMS OF USE
# =========================================================

@app.route('/terms')
def terms():

    return render_template(

        'terms.html',

        ui=get_ui()
    )


# =========================================================
# ✉️ CONTACT
# =========================================================

@app.route('/contact')
def contact():

    return render_template(

        'contact.html',

        ui=get_ui()
    )

# =========================================================
# ⚠ ERROR HANDLER
# =========================================================

@app.errorhandler(Exception)
def handle_error(e):

    print("ERROR:", e)

    return f"""
    <h1>ERROR</h1>
    <pre>{str(e)}</pre>
    """, 500


# =========================================================
# ✅ CREATE DATABASE
# =========================================================

with app.app_context():

    db.create_all()


# =========================================================
# 🚀 RUN APP
# =========================================================

if __name__ == '__main__':

    port = int(
        os.environ.get("PORT", 5000)
    )

    app.run(

        host='0.0.0.0',

        port=port
    )