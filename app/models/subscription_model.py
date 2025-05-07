from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class SubscriptionModel(BaseModel):
    subscription_id: Optional[str] = Field(alias="_id")
    user_id: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    plan: str 
    status: str 