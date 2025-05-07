from fastapi import APIRouter, Depends
from app.services.read_news_service import ReadNewsService
from app.databases.mongodb import get_article_collection, get_user_collection

router = APIRouter()

@router.get("/read/{news_id}")
async def read_news(news_id: str, article_col=Depends(get_article_collection), user_col=Depends(get_user_collection)):
    service = ReadNewsService(article_col, user_col)
    return await service.show_news(news_id)
