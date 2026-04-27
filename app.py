from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = "secret123"  # required for session

questions = [
    {
        "question": "You must always carry your driver’s license while driving.",
        "choices": ["True", "False"],
        "answer": "True",
        "explanation": "Driving without your license is illegal in Japan."
    },
    {
        "question": "You can ignore traffic signs if no police are present.",
        "choices": ["True", "False"],
        "answer": "False",
        "explanation": "Traffic rules must always be followed."
    }
]

@app.route('/')
def start():
    session['answers'] = []
    session['current'] = 0
    return redirect('/question')


@app.route('/question', methods=['GET', 'POST'])
def question():
    if request.method == 'POST':
        answer = request.form.get('answer')
        session['answers'].append(answer)
        session['current'] += 1

    if session['current'] >= len(questions):
        return redirect('/result')

    q = questions[session['current']]
    return render_template('question.html', q=q, index=session['current'])


@app.route('/result')
def result():
    results = []
    score = 0

    for i, q in enumerate(questions):
        user_answer = session['answers'][i]
        correct = (user_answer or "").strip().lower() == q["answer"].strip().lower()

        if correct:
            score += 1

        results.append({
            "question": q["question"],
            "your_answer": user_answer,
            "correct_answer": q["answer"],
            "explanation": q["explanation"],
            "is_correct": correct
        })

    return render_template('result.html', score=score, total=len(questions), results=results)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)