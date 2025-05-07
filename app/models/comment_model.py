from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class CommentModel(BaseModel):
    comment_id: Optional[str] = Field(alias="_id")
    news_id: str
    user_id: str
    content: str
    comment_date: Optional[date] = None
    is_approved: bool = True