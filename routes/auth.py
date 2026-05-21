from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from models import (
    User,
    db
)

from extensions import (
    mail,
    serializer
)

from languages.ui import get_ui

auth = Blueprint(
    'auth',
    __name__
)

@auth.route('/test-auth')
def test_auth():

    return """
    <h1>
    ✅ Auth Blueprint Works
    </h1>
    """

# =========================================================
# 👤 LOGIN
# =========================================================

@auth.route('/login', methods=['GET', 'POST'])
def login():

    ui = get_ui()

    error = None

    if request.method == 'POST':

        email = (
            request.form.get('email')
            .strip()
            .lower()
        )

        password = request.form.get(
            'password'
        )

        user = User.query.filter_by(
            email=email
        ).first()

        if user and check_password_hash(
            user.password,
            password
        ):

            # ✅ LOGIN USER

            session['user_id'] = user.id

            session['username'] = (
                user.username
            )

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
# 👤 REGISTER
# =========================================================

@auth.route('/register', methods=['GET', 'POST'])
def register():

    ui = get_ui()

    error = None

    success = None

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

        password = request.form.get(
            'password'
        )

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

                    password=hashed,

                    is_verified=True
                )

                db.session.add(new_user)

                db.session.commit()

                print("AUTO VERIFIED USER")

                success = (
                    "Account created successfully. "
                    "You can now login."
                )

    return render_template(

        'register.html',

        error=error,

        success=success,

        ui=ui
    )

# =========================================================
# 🚪 LOGOUT
# =========================================================

@auth.route('/logout')
def logout():

    session.clear()

    return redirect('/menu')

# =========================================================
# 🔑 FORGOT PASSWORD
# =========================================================

@auth.route(
    '/forgot-password',
    methods=['GET', 'POST']
)
def forgot_password():

    message = None

    if request.method == 'POST':

        email = (
            request.form.get('email')
            .strip()
            .lower()
        )

        user = User.query.filter_by(
            email=email
        ).first()

        if user:

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
Reset your password:

{reset_link}

If you did not request this,
ignore this email.
"""

            send_email(

                'Reset Password',

                email,

                body
            )

        message = (
            "If the email exists, "
            "a reset link was sent."
        )

    return render_template(

        'forgot_password.html',

        message=message,

        ui=get_ui()
    )
