from pymongo.collection import Collection
from typing import Optional, List

class StatisticsRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def get_by_id(self, stats_id: str) -> Optional[dict]:
        """Lấy thống kê theo ID."""
        return await self.collection.find_one({"_id": stats_id})

    async def get_by_news_id(self, news_id: str) -> Optional[dict]:
        """Lấy thống kê cho một bài viết tin tức cụ thể."""
        return await self.collection.find_one({"news_id": news_id})

    async def get_all(self) -> List[dict]:
        """Lấy tất cả thống kê."""
        return list(await self.collection.find())

    async def create(self, stats_data: dict) -> dict:
        """Tạo một thống kê mới."""
        result = await self.collection.insert_one(stats_data)
        inserted_id = result.inserted_id
        return await self.get_by_id(str(inserted_id))

    async def update(self, stats_id: str, stats_data: dict) -> Optional[dict]:
        """Cập nhật thống kê theo ID."""
        result = await self.collection.update_one({"_id": stats_id}, {"$set": stats_data})
        if result.modified_count > 0:
            return await self.get_by_id(stats_id)
        else:
            return None

    async def delete(self, stats_id: str) -> bool:
        """Xóa thống kê theo ID."""
        result = await self.collection.delete_one({"_id": stats_id})
        return result.deleted_count > 0

    async def increment_views(self, news_id: str) -> Optional[dict]:
        """Tăng số lượt xem cho một bài viết tin tức."""
        result = await self.collection.update_one(
            {"news_id": news_id}, {"$inc": {"views": 1}}
        )
        if result.modified_count > 0:
            return await self.get_by_news_id(news_id)
        else:
            return None

    async def increment_likes(self, news_id: str) -> Optional[dict]:
        """Tăng số lượt thích cho một bài viết tin tức."""
        result = await self.collection.update_one(
            {"news_id": news_id}, {"$inc": {"likes": 1}}
        )
        if result.modified_count > 0:
             return await self.get_by_news_id(news_id)
        else:
            return None

    async def increment_comments(self, news_id: str) -> Optional[dict]:
        """Tăng số lượng bình luận cho một bài viết tin tức."""
        result = await self.collection.update_one(
            {"news_id": news_id}, {"$inc": {"comments": 1}}
        )
        if result.modified_count > 0:
            return await self.get_by_news_id(news_id)
        else:
            return None
