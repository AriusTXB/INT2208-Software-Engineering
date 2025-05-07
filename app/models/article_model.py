from pydantic import BaseModel, Field
from typing import List, Optional

class ArticleModel(BaseModel):
    id: Optional[str]
    title: str
    content: str
    is_premium: bool = False
    category: str
    tags: List[str] = []
    created_at: Optional[str]