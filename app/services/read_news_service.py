from app.repositories.article_repo import ArticleRepository
from app.repositories.user_repo import UserRepository

class ReadNewsService:
    def __init__(self, article_col, user_col):
        self.article_repo = ArticleRepository(article_col)
        self.user_repo = UserRepository(user_col)

    async def show_news(self, news_id: str):
        article = await self.article_repo.get_by_id(news_id)
        if article:
            await self.user_repo.add_read_history("dummy_user_id", news_id)  
        return article