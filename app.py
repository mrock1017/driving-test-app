from flask import Flask, render_template, request, redirect, session
import os
import json
import random
import time

def load_questions(filename):
    filepath = os.path.join("data", filename)

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


@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/quit')
def quit_exam():
    session.clear()  # clear all session data
    return redirect('/menu')


# ✅ START MODE
@app.route('/start/<mode>')
def start_mode(mode):
    questions = load_questions(f"{mode}.json")

    order = list(range(len(questions)))
    random.shuffle(order)

    session['answers'] = []
    session['current'] = 0
    session['mode'] = mode
    session['order'] = order

    # ⏱ Timer only for exam modes
    if mode != "reviewer":
        session['start_time'] = int(time.time())
        session['duration'] = 30 * 60  # 30 minutes

    print("MODE SET:", mode)

    return redirect('/question')


@app.route('/')
def start():
    return redirect('/menu')


# ✅ QUESTION PAGE
@app.route('/question', methods=['GET', 'POST'])
def question():
    if 'mode' not in session:
        return redirect('/menu')

    questions = load_questions(f"{session['mode']}.json")
    order = session.get('order', list(range(len(questions))))

    if len(questions) == 0:
        return "<h2>No questions found.</h2><a href='/menu'>Go back</a>"

    is_reviewer = session['mode'] == "reviewer"

    # ⏱ Only apply timer in exam mode
    remaining = None
    if not is_reviewer:
        start_time = session.get('start_time', int(time.time()))
        duration = session.get('duration', 1800)
        remaining = duration - (int(time.time()) - start_time)

        if remaining <= 0:
            return redirect('/result')

    feedback = False
    correct_answer = None
    explanation = None
    is_correct = None
    user_answer = None

    if request.method == 'POST':
        answer = request.form.get('answer')

        if answer is not None:
            idx = order[session['current']]
            q = questions[idx]

            correct_answer = q["answer"]
            explanation = q["explanation"]
            user_answer = answer

            is_correct = answer.strip().lower() == correct_answer.strip().lower()

            if not is_reviewer:
                session['answers'].append(answer)
                session['current'] += 1
                return redirect('/question')
            else:
                feedback = True  # stay on same question

    if session['current'] >= len(order):
        return redirect('/result')

    idx = order[session['current']]
    q = questions[idx]

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


# ➡️ NEXT QUESTION (for reviewer mode)
@app.route('/next')
def next_question():
    session['current'] += 1
    return redirect('/question')


# ✅ RESULT PAGE (exam only)
@app.route('/result')
def result():
    if 'mode' not in session:
        return redirect('/menu')

    # reviewer doesn't need result page
    if session['mode'] == "reviewer":
        return redirect('/menu')

    questions = load_questions(f"{session['mode']}.json")
    order = session.get('order', list(range(len(questions))))

    results = []
    score = 0

    for i, idx in enumerate(order):
        q = questions[idx]
        user_answer = session['answers'][i] if i < len(session['answers']) else None

        correct = (user_answer or "").strip().lower() == q["answer"].strip().lower()

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

    passing_score = int(len(order) * 0.9)
    passed = score >= passing_score

    return render_template(
        'result.html',
        score=score,
        total=len(order),
        results=results,
        passed=passed,
        passing_score=passing_score
    )


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)