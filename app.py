from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

import os
import json
import random
import time

app = Flask(__name__)

# ✅ SECRET KEY
app.config['SECRET_KEY'] = 'secret123'

# ✅ DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ✅ DEBUG
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
        db.String(200),
        nullable=False
    )

    is_premium = db.Column(
        db.Boolean,
        default=False
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
            "You correctly understood the road rule and selected "
            f"the proper answer ({correct_answer}). "
            "This question tests safety awareness, "
            "traffic law understanding, and defensive driving."
        )

    return (
        f"❌ Your answer was '{user_answer}', "
        f"but the correct answer is '{correct_answer}'. "
        "Focus carefully on road signs, pedestrian safety, "
        "hazard prediction, and proper driving judgment."
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

    print("TRYING:", filepath)

    # 🌐 fallback to English
    if not os.path.exists(filepath):

        filepath = os.path.join(
            "data",
            folder,
            "en",
            filename
        )

    print("LOADING:", filepath)

    if not os.path.exists(filepath):

        print("FILE NOT FOUND")

        return []

    try:

        with open(
            filepath,
            encoding="utf-8-sig"
        ) as f:

            data = json.load(f)

            print("QUESTIONS:", len(data))

            return data

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

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        existing = User.query.filter_by(
            email=email
        ).first()

        if existing:

            error = "Email already exists."

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

        email = request.form.get('email')
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
            session['is_premium'] = user.is_premium

            return redirect('/menu')

        else:

            error = "Invalid login credentials."

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
# 🌙 DARK MODE
# =========================================================

@app.route('/toggle-dark-mode')
def toggle_dark_mode():

    current = session.get(
        'dark_mode',
        False
    )

    session['dark_mode'] = not current

    return redirect('/menu')


# =========================================================
# ❌ QUIT EXAM
# =========================================================

@app.route('/quit')
def quit_exam():

    session.pop('mode', None)
    session.pop('answers', None)
    session.pop('current', None)
    session.pop('order', None)

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

    # 🏁 HONMEN
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

        order = selected_normal + selected_grouped

        session['duration'] = 50 * 60

    else:

        total_questions = 50

        if len(questions) > total_questions:

            order = random.sample(
                range(len(questions)),
                total_questions
            )

        else:

            order = list(range(len(questions)))

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

    # =====================================================
    # ✅ FORM SUBMIT
    # =====================================================

    if request.method == 'POST':

        answer = request.form.get('answer')

        if answer:

            correct_answer = q["answer"]

            explanation = q["explanation"]

            user_answer = answer

            is_correct = (

                answer.strip().lower()

                ==

                correct_answer.strip().lower()
            )

            ai_explanation = generate_ai_explanation(

                q["question"],

                correct_answer,

                user_answer,

                is_correct
            )

            # 🧠 REVIEWER MODE
            if is_reviewer:

                feedback = True

            # 📝 EXAM MODE
            else:

                session['answers'].append(answer)

                session['current'] += 1

                session.modified = True

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

    results = []

    score = 0
    total_questions = 0

    for i, idx in enumerate(order):

        q = questions[idx]

        user_answer = None

        if i < len(session['answers']):

            user_answer = session['answers'][i]

        total_questions += 1

        correct = (

            (user_answer or "").strip().lower()

            ==

            q["answer"].strip().lower()
        )

        if correct:

            score += 1

        results.append({

            "question": q["question"],

            "your_answer": user_answer,

            "correct_answer": q["answer"],

            "explanation": q["explanation"],

            "is_correct": correct,

            "image": q.get("image")
        })

    session['last_score'] = score
    session['last_total'] = total_questions

    passing_score = int(total_questions * 0.9)

    if session['mode'] == "honmen":

        passing_score = 90

    passed = score >= passing_score

    # 📊 HISTORY

    if 'score_history' not in session:

        session['score_history'] = []

    session['score_history'].append({

        "mode": session['mode'],

        "score": score,

        "total": total_questions,

        "passed": passed,

        "time": time.strftime(
            "%Y-%m-%d %H:%M"
        )
    })

    session['score_history'] = (
        session['score_history'][-20:]
    )

    session.modified = True

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

    history = session.get(
        'score_history',
        []
    )

    return render_template(

        'history.html',

        history=history[::-1],

        ui=get_ui()
    )


# =========================================================
# ⚠ ERROR HANDLER
# =========================================================

@app.errorhandler(Exception)
def handle_error(e):

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