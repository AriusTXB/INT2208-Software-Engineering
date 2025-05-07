from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class PendingArticleModel(BaseModel):
    pending_id: Optional[str] = Field(alias="_id")
    user_id: str
    title: str
    content: str
    submission_date: Optional[date] = None
    status: str 
    reviewed_by_admin_id: Optional[str] = None