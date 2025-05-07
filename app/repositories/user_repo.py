class UserRepository:
    def __init__(self, collection):
        self.col = collection

    async def get_by_id(self, user_id: str):
        return await self.col.find_one({"_id": user_id})

    async def update_profile(self, user_id: str, data: dict):
        return await self.col.update_one({"_id": user_id}, {"$set": data})

    async def delete_user(self, user_id: str):
        return await self.col.delete_one({"_id": user_id})

    async def add_read_history(self, user_id: str, news_id: str):
        return await self.col.update_one({"_id": user_id}, {"$addToSet": {"read_history": news_id}})