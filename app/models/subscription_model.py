from pydantic import BaseModel
from typing import Optional

class SubscriptionModel(BaseModel):
    id: Optional[str]
    user_id: str
    start_date: str
    end_date: Optional[str]
    active: bool = True