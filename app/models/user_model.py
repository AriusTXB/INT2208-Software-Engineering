from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

class UserModel(BaseModel):
    user_id: Optional[str] = Field(alias="_id")
    username: str
    email: str
    password_hash: str
    signup_date: Optional[date] = None
    last_login: Optional[date] = None
    subscription_status: Optional[str] = None
    favorite_articles: List[str] = []
    read_history: List[str] = []