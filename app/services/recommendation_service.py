from app.repositories.article_repo import ArticleRepository
from app.repositories.user_repo import UserRepository

class RecommendationService:
    def __init__(self, article_col, user_col):
        self.article_repo = ArticleRepository(article_col)
        self.user_repo = UserRepository(user_col)

    async def recommend_for_user(self, user_id: str):
        user = await self.user_repo.get_by_id(user_id)
        read_history = user.get("read_history", []) if user else []
        recommendations = await self.article_repo.col.find({"_id": {"$nin": read_history}}).to_list(10)
        return recommendations
