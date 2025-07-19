from sqlalchemy.orm import Session
from . import models
from datetime import datetime, timedelta


def get_challenge_quota(db: Session, user_id: str):
    return (
        db.query(models.ChallengeQuota)
        .filter(models.ChallengeQuota.user_id == user_id)
        .first()
    )


def create_challenge_quota(db: Session, user_id: str):
    db_quota = models.ChallengeQuota(user_id=user_id)
    db.add(db_quota)  # staged, ready to be committed
    db.commit()  # committed to the database
    db.refresh(db_quota)  # refresh the instance from the database
    return db_quota


def reset_quota(db: Session, quota: models.ChallengeQuota):
    now = datetime.now()
    if now - quota.last_reset_date > timedelta(hours=24):
        quota.last_reset_date = now
        quota.remaining_quota = 50
        db.commit()
        db.refresh(quota)
    return quota


def create_challenge(
    db: Session,
    difficulty: str,
    created_by: str,
    title: str,
    options: str,
    correct_answer_id: int,
    explanation: str,
):
    db_challenge = models.Challenge(
        difficulty=difficulty,
        created_by=created_by,
        title=title,
        options=options,
        correct_answer_id=correct_answer_id,
        explanation=explanation,
    )
    db.add(db_challenge)
    db.commit()
    db.refresh(db_challenge)
    return db_challenge


def get_user_challenges(db: Session, user_id: str):
    return (
        db.query(models.Challenge).filter(models.Challenge.created_by == user_id).all()
    )
