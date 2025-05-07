from fastapi import APIRouter, Depends
from app.services.statistics_service import StatisticsService
from app.databases.mongodb import get_stats_collection

router = APIRouter()

@router.get("/stats/user")
async def get_user_stats(user_id: str, stats_col=Depends(get_stats_collection)):
    return await StatisticsService(stats_col).get_user_stats(user_id)

@router.get("/stats/global")
async def get_global_stats(stats_col=Depends(get_stats_collection)):
    return await StatisticsService(stats_col).get_global_stats()