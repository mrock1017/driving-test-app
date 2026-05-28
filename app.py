from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    url_for
)

from models import db
from models import User
from flask_mail import (
    Mail,
    Message
)

from itsdangerous import (
    URLSafeTimedSerializer
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from extensions import (
    mail,
)

from languages.ui import get_ui

from routes.premium import premium
from utils.questions import load_questions
from routes.auth import auth
from routes.tests import tests
from config import Config
from models import db

import os
import json
import random
import time

app = Flask(__name__)

app.config.from_object(Config)

# =========================================================
# 🔄 AUTO PREMIUM SESSION SYNC
# =========================================================

@app.before_request
def sync_premium_session():

    if 'user_id' not in session:

        return

    user = User.query.get(
        session['user_id']
    )

    if not user:

        session.clear()

        return

    session['is_premium'] = (
        user.is_premium
    )

    session['subscription_status'] = (
        user.subscription_status
    )

app.register_blueprint(auth)
app.register_blueprint(tests)
app.register_blueprint(premium)

# =========================================================
# ✅ DATABASE
# =========================================================

database_url = os.environ.get(
    'DATABASE_URL'
)

# ✅ Railway PostgreSQL Fix

if database_url and database_url.startswith(
    "postgres://"
):

    database_url = database_url.replace(
        "postgres://",
        "postgresql://",
        1
    )

app.config['SQLALCHEMY_DATABASE_URI'] = (
    database_url
    or
    'sqlite:///users.db'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# =========================================================
# 📧 EMAIL CONFIG
# =========================================================

app.config['MAIL_SERVER'] = 'smtp-relay.brevo.com'

app.config['MAIL_PORT'] = 587

app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USE_SSL'] = False

app.config['MAIL_USERNAME'] = os.environ.get(
    'MAIL_USERNAME'
)

app.config['MAIL_PASSWORD'] = os.environ.get(
    'MAIL_PASSWORD'
)

app.config['MAIL_DEFAULT_SENDER'] = os.environ.get(
    'MAIL_DEFAULT_SENDER'
)

# ✅ IMPORTANT
mail.init_app(app)

# =========================================================
# 🔐 TOKEN SERIALIZER
# =========================================================

serializer = URLSafeTimedSerializer(
    app.config['SECRET_KEY']
)

# =========================================================
# ✅ DEBUG
# =========================================================

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = False

# =========================================================
# 👤 USER MODEL
# =========================================================

# =========================================================
# 🔐 LOGIN REQUIRED
# =========================================================

def login_required():

    if 'user_id' not in session:

        return redirect('/login')

# =========================================================
# 📧 SEND EMAIL
# =========================================================

def send_email(subject, recipient, body):

    try:

        msg = Message(

            subject,

            recipients=[recipient]
        )

        msg.body = body

        mail.send(msg)

        return True

    except Exception as e:

        print(e)

        return redirect('/menu')
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
# 📧 VERIFY EMAIL
# =========================================================

@app.route('/verify-email/<token>')
def verify_email(token):

    try:

        email = serializer.loads(

            token,

            salt='email-verify',

            max_age=3600
        )

        user = User.query.filter_by(
            email=email
        ).first()

        if user:

            user.is_verified = True

            db.session.commit()

            return """
            <h1>Email Verified</h1>
            <p>You can now login.</p>
            """

    except Exception as e:

        import traceback

        traceback.print_exc()

        raise e

# =========================================================
#  FORGOT PASSWORD
# =========================================================

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():

    error = None
    success = None

    if request.method == 'POST':

        email = request.form.get('email')

        user = User.query.filter_by(
            email=email
        ).first()

        if not user:

            error = "No account found with that email."

        else:

            token = serializer.dumps(
                email,
                salt='reset-password'
            )

            reset_link = url_for(
                'reset_password',
                token=token,
                _external=True
            )

            body = f"""
Hello,

Click the link below to reset your password:

{reset_link}

If you did not request this,
please ignore this email.
"""

            success_send = send_email(

                "Password Reset",

                email,

                body
            )

            if success_send:

                success = (
                    "Password reset email sent."
                )

            else:

                error = (
                    "Failed to send email."
                )

    return render_template(

        'forgot_password.html',

        error=error,

        success=success,

        ui=get_ui()
    )

# =========================================================
# 🔑 RESET PASSWORD
# =========================================================

@app.route(
    '/reset-password/<token>',
    methods=['GET', 'POST']
)
def reset_password(token):

    error = None

    success = None

    try:

        email = serializer.loads(

            token,

            salt='reset-password',

            max_age=3600
        )

    except:

        return """
        <h1>Invalid or Expired Link</h1>
        """

    if request.method == 'POST':

        password = request.form.get(
            'password'
        )

        if len(password) < 6:

            error = (
                "Password must be at least "
                "6 characters."
            )

        else:

            user = User.query.filter_by(
                email=email
            ).first()

            if user:

                user.password = (
                    generate_password_hash(
                        password
                    )
                )

                db.session.commit()

                success = (
                    "Password updated successfully."
                )

    return render_template(

        'reset_password.html',

        error=error,

        success=success,

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
# 🖼 FAVICON
# =========================================================

@app.route('/favicon.ico')
def favicon():

    return redirect(
        url_for(
            'static',
            filename='images/icon.png'
        )
    )

# =========================================================
# 🚀 RUN APP
# =========================================================

if __name__ == '__main__':

    port = int(
        os.environ.get("PORT", 5000)
    )

    app.run(
        host='0.0.0.0',
        port=port,
        debug=True
    )