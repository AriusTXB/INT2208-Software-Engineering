from pydantic import BaseModel
from typing import Dict, Optional

class StatisticsModel(BaseModel):
    id: Optional[str]
    user_id: Optional[str]
    article_reads: Dict[str, int] = {}  # news_id -> read count
    last_active: Optional[str]
    total_read_count: int = 0