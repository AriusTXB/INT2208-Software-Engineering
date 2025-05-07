from pymongo.collection import Collection
from typing import Optional, List

class ReportRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def get_by_id(self, report_id: str) -> Optional[dict]:
        """Lấy báo cáo theo ID."""
        return await self.collection.find_one({"_id": report_id})

    async def get_all(self) -> List[dict]:
        """Lấy tất cả báo cáo."""
        return list(await self.collection.find())

    async def create(self, report_data: dict) -> dict:
        """Tạo một báo cáo mới."""
        result = await self.collection.insert_one(report_data)
        inserted_id = result.inserted_id
        return await self.get_by_id(str(inserted_id))

    async def update(self, report_id: str, report_data: dict) -> Optional[dict]:
        """Cập nhật báo cáo theo ID."""
        result = await self.collection.update_one({"_id": report_id}, {"$set": report_data})
        if result.modified_count > 0:
            return await self.get_by_id(report_id)
        else:
            return None

    async def delete(self, report_id: str) -> bool:
        """Xóa báo cáo theo ID."""
        result = await self.collection.delete_one({"_id": report_id})
        return result.deleted_count > 0
