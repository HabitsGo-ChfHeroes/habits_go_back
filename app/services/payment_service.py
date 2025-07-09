from sqlalchemy.orm import Session
from app.schemas.payment_schema import PaymentCreate, PaymentResponse
from app.repositories.payment_repository import create_payment, get_latest_payment_by_user_id

def create_payment_entry(db: Session, data: PaymentCreate) -> PaymentResponse:
    payment = create_payment(db, data)
    return PaymentResponse.model_validate(payment)

def get_user_latest_payment(db: Session, user_id: int) -> PaymentResponse | None:
    payment = get_latest_payment_by_user_id(db, user_id)
    if not payment:
        return None
    return PaymentResponse.model_validate(payment)