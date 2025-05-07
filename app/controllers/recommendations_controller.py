from fastapi import APIRouter, Depends
from app.services.recommendation_service import RCMNewsSystem
from app.databases.mongodb import get_news_collection, get_user_collection

router = APIRouter(prefix="/news")

@router.get("/{news_id}")
async def get_news(news_id: str, news_collection=Depends(get_news_collection), user_collection=Depends(get_user_collection)):
    return await RCMNewsSystem(news_collection, user_collection).get_news(news_id)

@router.get("/view/{news_id}")
async def view_news(news_: str, news_collection=Depends(get_news_collection), user_collection=Depends(get_user_collection)):
    return await RCMNewsSystem(news_collection, user_collection).show_news(news_id)
