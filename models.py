from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100)
    )

    email = db.Column(
        db.String(100),
        unique=True
    )

    password = db.Column(
        db.String(200)
    )

    is_verified = db.Column(
        db.Boolean,
        default=False
    )

    is_premium = db.Column(
        db.Boolean,
        default=False
    )

    stripe_customer_id = db.Column(
    db.String(200),
    nullable=True
    )

    stripe_subscription_id = db.Column(
        db.String(200),
        nullable=True
    )

    subscription_status = db.Column(
        db.String(50),
        default='inactive'
    )

    failed_login_attempts = db.Column(
    db.Integer,
    default=0
    )

    locked_until = db.Column(
        db.DateTime,
        nullable=True
    )

# =========================================================
# 📊 SCORE HISTORY MODEL
# =========================================================

class ScoreHistory(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )

    mode = db.Column(
        db.String(100)
    )

    score = db.Column(
        db.Integer
    )

    total = db.Column(
        db.Integer
    )

    passed = db.Column(
        db.Boolean
    )

    created_at = db.Column(
        db.DateTime,
        default=db.func.now()
    )

class UserDevice(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id')
    )

    device_token = db.Column(
        db.String(300)
    )

    user_agent = db.Column(
        db.String(500)
    )

    created_at = db.Column(
        db.DateTime,
        default=db.func.now()
    )