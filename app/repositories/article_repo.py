class ArticleRepository:
    def __init__(self, collection):
        self.col = collection

    async def get_by_id(self, article_id: str):
        return await self.col.find_one({"_id": article_id})
