from flask import Flask, render_template, request
import os

app = Flask(__name__)

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
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    results = []

    for i, q in enumerate(questions):
        user_answer = request.form.get(str(i))
        print("User Answer:", user_answer)
        print("Correct Answer:", q["answer"])
        
        correct = user_answer == q["answer"]

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
    app.run(host='0.0.0.0', port=port, debug=True)