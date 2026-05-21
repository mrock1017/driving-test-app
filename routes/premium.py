from flask import (
    Blueprint,
    render_template,
    redirect,
    session
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

    return render_template(

        'upgrade.html',

        ui=get_ui()
    )

# =========================================================
# 💳 SUBSCRIBE
# =========================================================

@premium.route('/subscribe')
def subscribe():

    if 'user_id' not in session:

        return redirect('/login')

    user = User.query.get(
        session['user_id']
    )

    if not user:

        return redirect('/login')

    # ✅ TEMP PREMIUM

    user.is_premium = True

    db.session.commit()

    session['is_premium'] = True

    return redirect('/menu')