from flask import (
    Blueprint,
    render_template,
    redirect,
    session,
    request
)

from models import (
    User,
    db
)

from languages.ui import get_ui

premium = Blueprint(
    'premium',
    __name__
)

# =========================================================
# ⭐ UPGRADE PAGE
# =========================================================

@premium.route('/upgrade')
def upgrade():

    platform = request.args.get(
        'platform',
        session.get('platform')
    )

    if platform:

        session['platform'] = platform

    return render_template(

        'upgrade.html',

        ui=get_ui(),

        platform=platform
    )

# =========================================================
# 💳 SUBSCRIBE
# =========================================================

@premium.route('/subscribe')
def subscribe():

    platform = request.args.get(
        'platform',
        session.get('platform')
    )

    # 🚫 BLOCK ANDROID APP
    if platform == 'android':

        return redirect(
            '/upgrade?platform=android'
        )

    if 'user_id' not in session:

        return redirect('/login')

    user = User.query.get(
        session['user_id']
    )

    if not user:

        return redirect('/login')

    user.is_premium = True

    db.session.commit()

    session['is_premium'] = True

    return redirect('/menu')