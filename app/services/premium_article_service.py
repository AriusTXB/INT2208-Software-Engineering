from app.repositories.news_article_repository import NewsArticleRepository

class PremiumArticleService:
    def __init__(self, article_col):
        self.repo = NewsArticleRepository(article_col)

    async def get_premium_articles(self, user_id: str):
        return await self.repo.get_all_premium()
