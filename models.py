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