from pymongo.collection import Collection
from typing import Optional, List

class UserRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def get_by_id(self, user_id: str) -> Optional[dict]:
        """Lấy người dùng theo ID."""
        return await self.collection.find_one({"_id": user_id})

    async def get_by_username(self, username: str) -> Optional[dict]:
        """Lấy người dùng theo tên người dùng."""
        return await self.collection.find_one({"username": username})

    async def get_all(self) -> List[dict]:
        """Lấy tất cả người dùng."""
        return list(await self.collection.find())

    async def create(self, user_data: dict) -> dict:
        """Tạo một người dùng mới."""
        result = await self.collection.insert_one(user_data)
        inserted_id = result.inserted_id
        return await self.get_by_id(str(inserted_id))

    async def update(self, user_id: str, user_data: dict) -> Optional[dict]:
        """Cập nhật người dùng theo ID."""
        result = await self.collection.update_one({"_id": user_id}, {"$set": user_data})
        if result.modified_count > 0:
            return await self.get_by_id(user_id)
        else:
            return None

    async def delete(self, user_id: str) -> bool:
        """Xóa người dùng theo ID."""
        result = await self.collection.delete_one({"_id": user_id})
        return result.deleted_count > 0
    
    async def update_favorite_articles(self, user_id: str, article_id: str, add: bool = True) -> Optional[dict]:
        """Thêm hoặc xóa một bài viết khỏi danh sách yêu thích của người dùng."""
        if add:
            result = await self.collection.update_one(
                {"_id": user_id}, {"$addToSet": {"favorite_articles": article_id}}
            )
        else:
            result = await self.collection.update_one(
                {"_id": user_id}, {"$pull": {"favorite_articles": article_id}}
            )
        if result.modified_count > 0:
            return await self.get_by_id(user_id)
        else:
            return None

    async def add_to_read_history(self, user_id: str, article_id: str) -> Optional[dict]:
        """Thêm một bài viết vào lịch sử đọc của người dùng."""
        result = await self.collection.update_one(
            {"_id": user_id}, {"$addToSet": {"read_history": article_id}}
        )
        if result.modified_count > 0:
            return await self.get_by_id(user_id)
        else:
            return None

