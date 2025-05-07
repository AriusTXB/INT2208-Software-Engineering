from pymongo.collection import Collection
from typing import Optional, List

class PaymentRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def get_by_id(self, payment_id: str) -> Optional[dict]:
        """Lấy thanh toán theo ID."""
        return await self.collection.find_one({"_id": payment_id})

    async def get_all(self) -> List[dict]:
        """Lấy tất cả thanh toán."""
        return list(await self.collection.find())

    async def create(self, payment_data: dict) -> dict:
        """Tạo một thanh toán mới."""
        result = await self.collection.insert_one(payment_data)
        inserted_id = result.inserted_id
        return await self.get_by_id(str(inserted_id))

    async def update(self, payment_id: str, payment_data: dict) -> Optional[dict]:
        """Cập nhật thanh toán theo ID."""
        result = await self.collection.update_one({"_id": payment_id}, {"$set": payment_data})
        if result.modified_count > 0:
            return await self.get_by_id(payment_id)
        else:
            return None

    async def delete(self, payment_id: str) -> bool:
        """Xóa thanh toán theo ID."""
        result = await self.collection.delete_one({"_id": payment_id})
        return result.deleted_count > 0