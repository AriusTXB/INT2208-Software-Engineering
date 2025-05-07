from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class ReportModel(BaseModel):
    report_id: Optional[str] = Field(alias="_id")
    user_id: str
    target_id: str  
    target_type: str  
    reason: str
    report_date: Optional[date] = None
    status: str