from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

class NewsArticleModel(BaseModel):
    news_id: Optional[str] = Field(alias="_id")  
    title: str
    content: str
    author: str
    category: str
    publication_date: Optional[date] = None
    tags: List[str] = []