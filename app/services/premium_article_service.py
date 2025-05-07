from app.repositories.article_repo import ArticleRepository

class PremiumArticleService:
    def __init__(self, article_col):
        self.repo = ArticleRepository(article_col)

    async def get_premium_articles(self, user_id: str):
        return await self.repo.get_all_premium()
