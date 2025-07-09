from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_session
from app.schemas.payment_schema import PaymentCreate, PaymentResponse
from app.services.payment_service import create_payment_entry, get_user_latest_payment

router = APIRouter()

@router.post("/membership", response_model=PaymentResponse)
def create_payment(data: PaymentCreate, db: Session = Depends(get_session)):
    return create_payment_entry(db, data)

@router.get("/membership/latest/{user_id}", response_model=PaymentResponse)
def get_latest_payment(user_id: int, db: Session = Depends(get_session)):
    payment = get_user_latest_payment(db, user_id)
    if not payment:
        raise HTTPException(status_code=404, detail="No se encontró un pago para este usuario")
    return payment
