from pymongo.collection import Collection
from typing import Optional, List

class PendingArticleRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def get_by_id(self, pending_id: str) -> Optional[dict]:
        """Lấy bài viết đang chờ duyệt theo ID."""
        return await self.collection.find_one({"_id": pending_id})

    async def get_all(self) -> List[dict]:
        """Lấy tất cả bài viết đang chờ duyệt."""
        return list(await self.collection.find())

    async def create(self, pending_article_data: dict) -> dict:
        """Tạo một bài viết đang chờ duyệt mới."""
        result = await self.collection.insert_one(pending_article_data)
        inserted_id = result.inserted_id
        return await self.get_by_id(str(inserted_id))

    async def update(self, pending_id: str, pending_article_data: dict) -> Optional[dict]:
        """Cập nhật bài viết đang chờ duyệt theo ID."""
        result = await self.collection.update_one({"_id": pending_id}, {"$set": pending_article_data})
        if result.modified_count > 0:
            return await self.get_by_id(pending_id)
        else:
            return None

    async def delete(self, pending_id: str) -> bool:
        """Xóa bài viết đang chờ duyệt theo ID."""
        result = await self.collection.delete_one({"_id": pending_id})
        return result.deleted_count > 0