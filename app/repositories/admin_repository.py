from pymongo.collection import Collection
from typing import Optional, List

class AdminRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def get_by_id(self, admin_id: str) -> Optional[dict]:
        """Lấy admin theo ID."""
        return await self.collection.find_one({"_id": admin_id})

    async def get_by_username(self, username: str) -> Optional[dict]:
        """Lấy admin theo tên người dùng."""
        return await self.collection.find_one({"username": username})

    async def get_all(self) -> List[dict]:
        """Lấy tất cả admin."""
        return list(await self.collection.find())

    async def create(self, admin_data: dict) -> dict:
        """Tạo một admin mới."""
        result = await self.collection.insert_one(admin_data)
        inserted_id = result.inserted_id
        return await self.get_by_id(str(inserted_id))

    async def update(self, admin_id: str, admin_data: dict) -> Optional[dict]:
        """Cập nhật admin theo ID."""
        result = await self.collection.update_one({"_id": admin_id}, {"$set": admin_data})
        if result.modified_count > 0:
            return await self.get_by_id(admin_id)
        else:
            return None

    async def delete(self, admin_id: str) -> bool:
        """Xóa admin theo ID."""
        result = await self.collection.delete_one({"_id": admin_id})
        return result.deleted_count > 0