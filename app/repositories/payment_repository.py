from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.models.payment import Payment
from app.schemas.payment_schema import PaymentCreate
from datetime import datetime, timedelta, timezone
from app.utils.time_utils import get_today_lima

def create_payment(db: Session, data: PaymentCreate) -> Payment:
    now_lima = get_today_lima()

    new_payment = Payment(
        user_id=data.user_id,
        amount=data.amount,
        currency=data.currency,
        start_date=now_lima,
        end_date=now_lima + timedelta(days=30),
    )
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment

def get_latest_payment_by_user_id(db: Session, user_id: int) -> Payment | None:
    return (
        db.query(Payment)
        .filter(Payment.user_id == user_id)
        .order_by(desc(Payment.start_date))
        .first()
    )