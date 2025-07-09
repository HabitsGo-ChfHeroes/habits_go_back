from datetime import datetime
from pydantic import BaseModel, ConfigDict
from decimal import Decimal

class PaymentBase(BaseModel):
    amount: Decimal = 9.00
    currency: str = "USD"

class PaymentCreate(PaymentBase):
    user_id: int

class PaymentResponse(PaymentBase):
    id: int
    user_id: int
    start_date: datetime
    end_date: datetime

    model_config = ConfigDict(from_attributes=True)