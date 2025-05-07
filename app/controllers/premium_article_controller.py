from fastapi import APIRouter, Depends
from app.services.premium_article_service import PremiumArticleService
from app.databases.mongodb import get_article_collection

router = APIRouter()

@router.get("/premium/articles")
async def get_premium_articles(user_id: str, article_col=Depends(get_article_collection)):
    return await PremiumArticleService(article_col).get_premium_articles(user_id)
