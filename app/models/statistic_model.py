from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class StatisticsModel(BaseModel):
    stats_id: Optional[str] = Field(alias="_id")
    news_id: str
    views: int = 0
    likes: int = 0
    comments: int = 0
    interactions: List[Dict[str, int]] = []  
