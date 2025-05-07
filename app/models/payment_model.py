from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from decimal import Decimal

class PaymentModel(BaseModel):
    payment_id: Optional[str] = Field(alias="_id")
    user_id: str
    subscription_id: str
    amount: Decimal = 0.0
    payment_date: Optional[date] = None
    payment_method: str  
