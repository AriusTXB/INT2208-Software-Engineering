from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class AdminModel(BaseModel):
    admin_id: Optional[str] = Field(alias="_id")
    username: str
    email: str
    password_hash: str
    role: str
    created_date: Optional[date] = None