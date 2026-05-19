from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

import os
import json
import random
import time

app = Flask(__name__)

# ✅ SECRET KEY
app.config['SECRET_KEY'] = 'secret123'

# ✅ DEBUG
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = False


# 👤 SIMPLE USER STORAGE
USERS = {

    "admin@example.com": {

        "username": "admin",

        "password": generate_password_hash(
            "1234"
        ),

        "is_premium": True
    }

}


# 🌐 UI TRANSLATIONS
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


# 🌐 GET UI LANGUAGE
def get_ui():

    language = session.get('lang', 'en')

    return UI_TEXT.get(
        language,
        UI_TEXT['en']
    )


# 🤖 AI EXPLANATION
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
            "This question checks safe driving awareness "
            "and traffic law understanding."
        )

    else:

        return (
            f"❌ Your answer was '{user_answer}', "
            f"but the correct answer is '{correct_answer}'. "
            "Focus carefully on road safety, signs, "
            "pedestrian awareness, and driving judgment."
        )


# ✅ LOAD QUESTIONS
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

        with open(filepath, encoding="utf-8-sig") as f:

            return json.load(f)

    except Exception as e:

        print(e)

        return []


# ✅ SET LANGUAGE
@app.route('/set-language/<lang>')
def set_language(lang):

    allowed_languages = ['en', 'tl', 'ne']

    if lang not in allowed_languages:

        lang = 'en'

    session['lang'] = lang

    session.modified = True

    return redirect('/menu')


# 👤 REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():

    ui = get_ui()

    error = None

    if request.method == 'POST':

        username = request.form.get('username')

        email = request.form.get('email')

        password = request.form.get('password')

        if email in USERS:

            error = "Email already exists."

        else:

            USERS[email] = {

                "username": username,

                "password": generate_password_hash(
                    password
                ),

                "is_premium": False
            }

            return redirect('/login')

    return render_template(
        'register.html',
        error=error,
        ui=ui
    )


# 👤 LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():

    ui = get_ui()

    error = None

    if request.method == 'POST':

        email = request.form.get('email')

        password = request.form.get('password')

        user = USERS.get(email)

        if user and check_password_hash(
            user['password'],
            password
        ):

            session['username'] = user['username']

            session['email'] = email

            session['is_premium'] = user['is_premium']

            return redirect('/menu')

        else:

            error = "Invalid login credentials."

    return render_template(
        'login.html',
        error=error,
        ui=ui
    )


# 🚪 LOGOUT
@app.route('/logout')
def logout():

    session.clear()

    return redirect('/menu')


# 🌙 DARK MODE
@app.route('/toggle-dark-mode')
def toggle_dark_mode():

    current = session.get(
        'dark_mode',
        False
    )

    session['dark_mode'] = not current

    return redirect('/menu')


# ✅ MENU
@app.route('/menu')
def menu():

    if 'lang' not in session:

        session['lang'] = 'en'

    return render_template(
        'menu.html',
        ui=get_ui()
    )


# ✅ HOME
@app.route('/')
def start():

    return redirect('/menu')


# ✅ QUIT EXAM
@app.route('/quit')
def quit_exam():

    keep_user = session.get('username')
    keep_email = session.get('email')
    keep_premium = session.get('is_premium')

    session.clear()

    if keep_user:

        session['username'] = keep_user
        session['email'] = keep_email
        session['is_premium'] = keep_premium

    return redirect('/menu')


# ✅ START MODE
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

        return "<h2>No questions found.</h2>"

    session['folder'] = folder
    session['questions_file'] = test

    session['answers'] = []
    session['current'] = 0
    session['mode'] = mode

    order = list(range(len(questions)))
    random.shuffle(order)

    session['order'] = order

    if "reviewer" not in mode:

        session['start_time'] = int(time.time())

        if mode == "honmen":

            session['duration'] = 50 * 60

        else:

            session['duration'] = 30 * 60

    return redirect('/question')


# ✅ QUESTION PAGE
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

    order = session['order']

    if session['current'] >= len(order):

        return redirect('/result')

    idx = order[session['current']]

    q = questions[idx]

    is_reviewer = (
        "reviewer" in session['mode']
    )

    feedback = False

    correct_answer = None
    explanation = None
    is_correct = None
    user_answer = None
    ai_explanation = None

    remaining = None

    if not is_reviewer:

        remaining = session['duration'] - (
            int(time.time()) - session['start_time']
        )

        if remaining <= 0:

            return redirect('/result')

    if request.method == 'POST':

        answer = request.form.get('answer')

        if answer:

            correct_answer = q["answer"]

            explanation = q["explanation"]

            user_answer = answer

            is_correct = (

                answer.strip().lower()

                ==

                q["answer"].strip().lower()
            )

            ai_explanation = generate_ai_explanation(

                q["question"],

                correct_answer,

                user_answer,

                is_correct
            )

            session['answers'].append(answer)

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


# ✅ NEXT QUESTION
@app.route('/next')
def next_question():

    session['current'] += 1

    return redirect('/question')


# ✅ RESULT PAGE
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

    order = session['order']

    score = 0

    results = []

    for i, idx in enumerate(order):

        q = questions[idx]

        if i >= len(session['answers']):

            break

        user_answer = session['answers'][i]

        correct = (

            user_answer.strip().lower()

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

    total_questions = len(results)

    session['last_score'] = score
    session['last_total'] = total_questions

    passing_score = int(total_questions * 0.9)

    passed = score >= passing_score

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


# 📊 SCORE HISTORY
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


# ✅ SHOW REAL ERRORS
@app.errorhandler(Exception)
def handle_error(e):

    return f"""
    <h1>ERROR</h1>
    <pre>{str(e)}</pre>
    """, 500


if __name__ == '__main__':

    port = int(
        os.environ.get("PORT", 5000)
    )

    app.run(
        host='0.0.0.0',
        port=port
    )