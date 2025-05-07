from pymongo.collection import Collection
from typing import Optional, List

class NewsArticleRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def get_by_id(self, news_id: str) -> Optional[dict]:
        """Lấy tin tức theo ID."""
        return await self.collection.find_one({"_id": news_id})

    async def get_all(self) -> List[dict]:
        """Lấy tất cả tin tức."""
        return list(await self.collection.find())

    async def create(self, article_data: dict) -> dict:
        """Tạo một tin tức mới."""
        result = await self.collection.insert_one(article_data)
        inserted_id = result.inserted_id
        return await self.get_by_id(str(inserted_id))

    async def update(self, news_id: str, article_data: dict) -> Optional[dict]:
        """Cập nhật tin tức theo ID."""
        result = await self.collection.update_one({"_id": news_id}, {"$set": article_data})
        if result.modified_count > 0:
            return await self.get_by_id(news_id)
        else:
            return None

    async def delete(self, news_id: str) -> bool:
        """Xóa tin tức theo ID."""
        result = await self.collection.delete_one({"_id": news_id})
        return result.deleted_count > 0