from pymongo.collection import Collection
from typing import Optional, List

class SubscriptionRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def get_by_id(self, subscription_id: str) -> Optional[dict]:
        """Lấy đăng ký theo ID."""
        return await self.collection.find_one({"_id": subscription_id})

    async def get_by_user_id(self, user_id: str) -> Optional[dict]:
        """Lấy một đăng ký theo ID người dùng. Hữu ích để tìm đăng ký hiện tại."""
        return await self.collection.find_one({"user_id": user_id})

    async def get_all(self) -> List[dict]:
        """Lấy tất cả đăng ký."""
        return list(await self.collection.find())

    async def create(self, subscription_data: dict) -> dict:
        """Tạo một đăng ký mới."""
        result = await self.collection.insert_one(subscription_data)
        inserted_id = result.inserted_id
        return await self.get_by_id(str(inserted_id))

    async def update(self, subscription_id: str, subscription_data: dict) -> Optional[dict]:
        """Cập nhật đăng ký theo ID."""
        result = await self.collection.update_one({"_id": subscription_id}, {"$set": subscription_data})
        if result.modified_count > 0:
            return await self.get_by_id(subscription_id)
        else:
            return None

    async def delete(self, subscription_id: str) -> bool:
        """Xóa đăng ký theo ID."""
        result = await self.collection.delete_one({"_id": subscription_id})
        return result.deleted_count > 0
