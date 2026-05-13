from flask import Flask, render_template, request, redirect, session
import os
import json
import random
import time

# ✅ LOAD QUESTIONS
def load_questions(folder, filename):

    filepath = os.path.join(
        "data",
        folder,
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
            return json.load(f)

    except Exception as e:
        print("JSON ERROR in", filepath, ":", e)
        return []


app = Flask(__name__)

app.secret_key = "secret123"

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True


# ✅ MENU
@app.route('/menu')
def menu():

    return render_template('menu.html')


# ✅ QUIT
@app.route('/quit')
def quit_exam():

    session.clear()

    return redirect('/menu')


# ✅ START MODE
@app.route('/start/<mode>/<test>')
def start_mode(mode, test):

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

            # 🏁 grouped questions
            if "question_group" in q:
                grouped_questions.append(i)

            # 📝 normal questions
            else:
                normal_questions.append(i)

        random.shuffle(normal_questions)
        random.shuffle(grouped_questions)

        # grouped always at end
        order = normal_questions + grouped_questions

        # ⏱ 50 mins
        session['start_time'] = int(time.time())
        session['duration'] = 50 * 60

    else:

        order = list(range(len(questions)))

        random.shuffle(order)

        # 🧠 reviewer
        if "reviewer" in mode:

            session['duration'] = None

        else:

            # ⏱ karimen
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

    questions = load_questions(
        session['folder'],
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
        user_answer=user_answer
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

    questions = load_questions(
        session['folder'],
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

            # ✅ each group = 2 points
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

                # ❌ one mistake = whole group wrong
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

            # ✅ full 2 points only if all correct
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

    # 🎯 HONMEN passing = 90/100
    if session['mode'] == "honmen":

        passing_score = 90

    else:

        passing_score = int(
            total_questions * 0.9
        )

    passed = score >= passing_score

    return render_template(
        'result.html',
        score=score,
        total=total_questions,
        results=results,
        passed=passed,
        passing_score=passing_score
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