from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class UserModel(BaseModel):
    id: Optional[str]
    email: EmailStr
    username: str
    hashed_password: str
    role: str = "viewer"
    read_history: List[str] = []
    is_subscribed: bool = False