from pymongo.collection import Collection
from typing import Optional, List

class CommentRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def get_by_id(self, comment_id: str) -> Optional[dict]:
        """Lấy bình luận theo ID."""
        return await self.collection.find_one({"_id": comment_id})

    async def get_by_news_id(self, news_id: str) -> List[dict]:
        """Lấy tất cả bình luận cho một bài viết tin tức nhất định."""
        return list(await self.collection.find({"news_id": news_id}))

    async def get_all(self) -> List[dict]:
        """Lấy tất cả bình luận."""
        return list(await self.collection.find())

    async def create(self, comment_data: dict) -> dict:
        """Tạo một bình luận mới."""
        result = await self.collection.insert_one(comment_data)
        inserted_id = result.inserted_id
        return await self.get_by_id(str(inserted_id))

    async def update(self, comment_id: str, comment_data: dict) -> Optional[dict]:
        """Cập nhật bình luận theo ID."""
        result = await self.collection.update_one({"_id": comment_id}, {"$set": comment_data})
        if result.modified_count > 0:
            return await self.get_by_id(comment_id)
        else:
            return None

    async def delete(self, comment_id: str) -> bool:
        """Xóa bình luận theo ID."""
        result = await self.collection.delete_one({"_id": comment_id})
        return result.deleted_count > 0
