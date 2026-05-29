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
    serializer,
    send_email
)

from languages.ui import get_ui

auth = Blueprint(
    'auth',
    __name__
)

from datetime import (
    datetime,
    timedelta
)

import uuid
from flask import make_response
from models import UserDevice

MAX_PREMIUM_DEVICES = 3

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

        # =====================================================
        # 🔒 ACCOUNT LOCK CHECK
        # =====================================================

        if user and user.locked_until:

            if datetime.utcnow() < user.locked_until:

                error = (
                    "Too many failed login attempts. "
                    "Please try again later."
                )

                return render_template(

                    'login.html',

                    error=error,

                    ui=ui
                )
        if user and check_password_hash(
            user.password,
            password
        ):
            # =====================================================
            # ✅ RESET FAILED ATTEMPTS
            # =====================================================

            user.failed_login_attempts = 0

            user.locked_until = None

            db.session.commit()

            # =====================================================
            # 📱 DEVICE LIMIT CHECK
            # =====================================================

            device_token = request.cookies.get(
                'device_token'
            )

            if not device_token:

                device_token = str(uuid.uuid4())

            existing_device = UserDevice.query.filter_by(

                user_id=user.id,

                device_token=device_token

            ).first()

            if not existing_device:

                device_count = UserDevice.query.filter_by(

                    user_id=user.id

                ).count()

                # =================================================
                # 🔒 PREMIUM DEVICE LIMIT
                # =================================================

                if user.is_premium:

                    if device_count >= MAX_PREMIUM_DEVICES:

                        return render_template(

                            'login.html',

                            error=(
                                "Maximum premium devices reached. "
                                "Please logout from another device first."
                            ),

                            ui=ui
                        )

                # =================================================
                # 💾 SAVE DEVICE
                # =================================================

                new_device = UserDevice(

                    user_id=user.id,

                    device_token=device_token,

                    user_agent=request.headers.get(
                        'User-Agent'
                    )
                )

                db.session.add(new_device)

                db.session.commit()

            # =====================================================
            # ✅ LOGIN USER
            # =====================================================

            session['user_id'] = user.id

            session['username'] = (
                user.username
            )

            session['is_premium'] = (
                user.is_premium
            )

            session['subscription_status'] = (
                user.subscription_status
            )

            # =====================================================
            # 🍪 SAVE DEVICE COOKIE
            # =====================================================

            response = make_response(

                redirect('/menu')
            )

            response.set_cookie(

                'device_token',

                device_token,

                max_age=60 * 60 * 24 * 365
            )

            return response

        else:

        # =================================================
        # ❌ FAILED LOGIN TRACKING
        # =================================================

            if user:

                user.failed_login_attempts += 1

                # =============================================
                # 🔒 LOCK AFTER 10 ATTEMPTS
                # =============================================

                if user.failed_login_attempts >= 10:

                    user.locked_until = (

                        datetime.utcnow()

                        + timedelta(minutes=15)
                    )

                db.session.commit()

            error = (
                "Invalid login credentials."
            )

    return render_template(

        'login.html',

        error=error,

        ui=ui
    )

# =========================================================
# 📱 MANAGE DEVICES
# =========================================================

@auth.route('/devices')
def devices():

    if 'user_id' not in session:

        return redirect('/login')

    devices = UserDevice.query.filter_by(

        user_id=session['user_id']

    ).order_by(

        UserDevice.created_at.desc()

    ).all()

    return render_template(

        'devices.html',

        devices=devices
    )

# =========================================================
# ❌ REMOVE DEVICE
# =========================================================

@auth.route('/remove-device/<int:device_id>')
def remove_device(device_id):

    if 'user_id' not in session:

        return redirect('/login')

    device = UserDevice.query.filter_by(

        id=device_id,

        user_id=session['user_id']

    ).first()

    if device:

        db.session.delete(device)

        db.session.commit()

    return redirect('/devices')

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

                # ✅ AUTO LOGIN

                session['user_id'] = new_user.id

                session['username'] = new_user.username

                session['is_premium'] = False

                device_token = str(uuid.uuid4())

                new_device = UserDevice(

                    user_id=new_user.id,

                    device_token=device_token,

                    user_agent=request.headers.get(
                        'User-Agent'
                    )
                )

                db.session.add(new_device)

                db.session.commit()

                response = make_response(

                    redirect('/menu')
                )

                response.set_cookie(

                    'device_token',

                    device_token,

                    max_age=60 * 60 * 24 * 365
                )

                return response

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

            
            success_send = send_email(

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

@auth.route('/delete-account')
def delete_account():

    return render_template(
        'delete_account.html'
    )