from flask import Flask, render_template, request, redirect, session
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

        # 🌙 DARK MODE
        "dark_mode": "🌙 Dark Mode",

        # 👤 LOGIN
        "login": "👤 Login",
        "logout": "🚪 Logout",
        "welcome": "Welcome"
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

        # 🌙 DARK MODE
        "dark_mode": "🌙 Dark Mode",

        # 👤 LOGIN
        "login": "👤 Login",
        "logout": "🚪 Logout",
        "welcome": "Maligayang pagdating"
    },

    "ne": {

        "study_mode": "🧠 अध्ययन मोड",
        "reviewer_karimen": "🧠 करिमेन रिभ्यू",
        "reviewer_honmen": "🧠 होनमेन रिभ्यू",

        "karimen_mock": "📝 करिमेन मोक टेस्ट",
        "karimen_test_1": "📝 करिमेन टेस्ट 1",
        "karimen_test_2": "📝 करिमेन टेस्ट 2",

        "honmen_mock": "🏁 होनमेन मोक टेस्ट",
        "honmen_test_1": "🏁 होनमेन टेस्ट 1",
        "honmen_test_2": "🏁 होनमेन टेस्ट 2",
        "honmen_test_3": "🏁 होनमेन टेस्ट 3",

        "app_info": "⚙️ एप जानकारी",
        "score_history": "📊 स्कोर इतिहास",
        "privacy": "🔒 गोपनीयता नीति",
        "terms": "📄 प्रयोगका सर्तहरू",
        "contact": "✉️ सम्पर्क गर्नुहोस्",

        # 🌙 DARK MODE
        "dark_mode": "🌙 डार्क मोड",

        # 👤 LOGIN
        "login": "👤 लगइन",
        "logout": "🚪 लगआउट",
        "welcome": "स्वागत छ"
    }
}


# 👤 SIMPLE USER DATABASE
USERS = {

    "admin": "1234",

    "demo": "demo123"
}


# ✅ LOAD QUESTIONS
def load_questions(folder, language, filename):

    filepath = os.path.join(
        "data",
        folder,
        language,
        filename
    )

    print("TRYING:", filepath)

    # 🌐 FALLBACK TO ENGLISH
    if not os.path.exists(filepath):

        print("FALLBACK TO ENGLISH")

        filepath = os.path.join(
            "data",
            folder,
            "en",
            filename
        )

    print("LOADING:", filepath)

    if not os.path.exists(filepath):

        print("FILE NOT FOUND:", filepath)

        return []

    if os.path.getsize(filepath) == 0:

        print("EMPTY FILE:", filepath)

        return []

    try:

        with open(filepath, encoding="utf-8-sig") as f:

            data = json.load(f)

            print("QUESTIONS LOADED:", len(data))

            return data

    except Exception as e:

        print("JSON ERROR in", filepath, ":", e)

        return []


# 🌐 GET UI LANGUAGE
def get_ui():

    language = session.get('lang', 'en')

    return UI_TEXT.get(
        language,
        UI_TEXT['en']
    )


# ✅ SET LANGUAGE
@app.route('/set-language/<lang>')
def set_language(lang):

    allowed_languages = ['en', 'tl', 'ne']

    print("CLICKED LANGUAGE:", lang)

    if lang not in allowed_languages:

        print("INVALID LANGUAGE")

        lang = 'en'

    session['lang'] = lang

    session.modified = True

    print("LANGUAGE SAVED:", session['lang'])

    return redirect('/menu')


# 👤 LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():

    ui = get_ui()

    error = None

    if request.method == 'POST':

        username = request.form.get(
            'username'
        )

        password = request.form.get(
            'password'
        )

        if username in USERS and USERS[username] == password:

            session['user'] = username

            return redirect('/menu')

        else:

            error = "Invalid username or password"

    return render_template(
        'login.html',
        error=error,
        ui=ui
    )


# 🚪 LOGOUT
@app.route('/logout')
def logout():

    session.pop('user', None)

    return redirect('/menu')


# ✅ MENU
@app.route('/menu')
def menu():

    if 'lang' not in session:

        session['lang'] = 'en'

    print("CURRENT LANGUAGE:", session['lang'])

    ui = get_ui()

    return render_template(
        'menu.html',
        ui=ui
    )


# ✅ QUIT
@app.route('/quit')
def quit_exam():

    session.clear()

    return redirect('/menu')


# ✅ START MODE
@app.route('/start/<mode>/<test>')
def start_mode(mode, test):

    language = session.get('lang', 'en')

    # 📝 KARIMEN
    if mode == "karimen":

        folder = "karimen"

    # 🏁 HONMEN
    elif mode == "honmen":

        folder = "honmen"

    # 🧠 REVIEWER KARIMEN
    elif mode == "reviewer_karimen":

        folder = "reviewer/karimen"

    # 🧠 REVIEWER HONMEN
    elif mode == "reviewer_honmen":

        folder = "reviewer/honmen"

    else:

        return "Invalid mode"

    questions = load_questions(
        folder,
        language,
        f"{test}.json"
    )

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

        session['start_time'] = int(time.time())

        session['duration'] = 50 * 60

    else:

        TOTAL_QUESTIONS = 50

        if len(questions) > TOTAL_QUESTIONS:

            order = random.sample(

                range(len(questions)),

                TOTAL_QUESTIONS
            )

        else:

            order = list(range(len(questions)))

            random.shuffle(order)

        # 🧠 reviewer
        if "reviewer" in mode:

            session['duration'] = None

        else:

            session['start_time'] = int(time.time())

            session['duration'] = 30 * 60

    session['order'] = order

    print("MODE SET:", mode)

    print("TOTAL QUESTIONS:", len(order))

    return redirect('/question')


# ✅ HOME
@app.route('/')
def start():

    return redirect('/menu')


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

    order = session.get(

        'order',

        list(range(len(questions)))
    )

    # ❌ no questions
    if len(questions) == 0:

        return "<h2>No questions found.</h2>"

    # ✅ finished
    if session['current'] >= len(order):

        return redirect('/result')

    is_reviewer = (

        "reviewer" in session['mode']
    )

    # ⏱ timer
    remaining = None

    if not is_reviewer:

        start_time = session.get(

            'start_time',

            int(time.time())
        )

        duration = session.get(

            'duration',

            1800
        )

        remaining = duration - (

            int(time.time()) - start_time
        )

        if remaining <= 0:

            return redirect('/result')

    # current question
    idx = order[session['current']]

    q = questions[idx]

    # reviewer mode feedback
    feedback = False

    correct_answer = None

    explanation = None

    is_correct = None

    user_answer = None

    # 🤖 AI EXPLANATION
    ai_explanation = None

    # ✅ FORM SUBMIT
    if request.method == 'POST':

        # 🏁 GROUP QUESTIONS
        if "items" in q:

            group_answers = []

            for item in q["items"]:

                ans = request.form.get(

                    f'answer_{item["number"]}'
                )

                group_answers.append(ans)

            session['answers'].append(

                group_answers
            )

            session.modified = True

            session['current'] += 1

            return redirect('/question')

        # 📝 NORMAL QUESTIONS
        else:

            answer = request.form.get(

                'answer'
            )

            if answer is not None:

                correct_answer = q["answer"]

                explanation = q["explanation"]

                user_answer = answer

                is_correct = (

                    answer.strip().lower()

                    ==

                    q["answer"].strip().lower()
                )

                # 🤖 AI EXPLANATION
                if is_correct:

                    ai_explanation = (
                        "✅ Great job! "
                        "You understood the traffic rule correctly."
                    )

                else:

                    ai_explanation = (
                        "❌ Review this rule carefully. "
                        "Focus on road safety, signs, and driving judgment."
                    )

                # 📝 exam mode
                if not is_reviewer:

                    session['answers'].append(

                        answer
                    )

                    session.modified = True

                    session['current'] += 1

                    return redirect('/question')

                # 🧠 reviewer mode
                else:

                    feedback = True

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

        ai_explanation=ai_explanation
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

    # 🧠 reviewer skips results
    if "reviewer" in session['mode']:

        return redirect('/menu')

    language = session.get('lang', 'en')

    questions = load_questions(

        session['folder'],

        language,

        f"{session['questions_file']}.json"
    )

    order = session.get(

        'order',

        list(range(len(questions)))
    )

    results = []

    score = 0

    total_questions = 0

    for i, idx in enumerate(order):

        q = questions[idx]

        user_answer = (

            session['answers'][i]

            if i < len(session['answers'])

            else None
        )

        # 🏁 GROUP QUESTIONS
        if "items" in q:

            total_questions += 2

            all_correct = True

            for j, item in enumerate(q["items"]):

                ans = None

                if (

                    isinstance(user_answer, list)

                    and j < len(user_answer)
                ):

                    ans = user_answer[j]

                correct = (

                    (ans or "").strip().lower()

                    ==

                    item["answer"].strip().lower()
                )

                if not correct:

                    all_correct = False

                results.append({

                    "question":

                        f"Group "

                        f"{q['question_group']} - "

                        f"{item['number']}: "

                        f"{item['question']}",

                    "your_answer":

                        ans,

                    "correct_answer":

                        item["answer"],

                    "explanation":

                        item["explanation"],

                    "is_correct":

                        correct,

                    "image":

                        q.get("image")
                })

            if all_correct:

                score += 2

        # 📝 NORMAL QUESTIONS
        else:

            total_questions += 1

            correct = (

                (user_answer or "").strip().lower()

                ==

                q["answer"].strip().lower()
            )

            if correct:

                score += 1

            results.append({

                "question":

                    q["question"],

                "your_answer":

                    user_answer,

                "correct_answer":

                    q["answer"],

                "explanation":

                    q["explanation"],

                "is_correct":

                    correct,

                "image":

                    q.get("image")
            })

    # 🎯 save latest score
    session['last_score'] = score

    session['last_total'] = total_questions

    # 🎯 PASSING SCORE
    if session['mode'] == "honmen":

        passing_score = 90

    else:

        passing_score = int(

            total_questions * 0.9
        )

    passed = score >= passing_score

    # 📊 SCORE HISTORY
    if 'score_history' not in session:

        session['score_history'] = []

    history_item = {

        "mode": session['mode'],

        "score": score,

        "total": total_questions,

        "passed": passed,

        "time": time.strftime(
            "%Y-%m-%d %H:%M"
        )
    }

    session['score_history'].append(
        history_item
    )

    # 🧹 KEEP LAST 20
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

        passing_score=passing_score
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

        history=history[::-1]
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