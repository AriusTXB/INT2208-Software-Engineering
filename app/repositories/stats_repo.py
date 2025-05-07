class StatisticsRepository:
    def __init__(self, collection):
        self.col = collection

    async def get_user_stats(self, user_id: str):
        return await self.col.find_one({"user_id": user_id})

    async def get_global_stats(self):
        return await self.col.find({"user_id": {"$exists": False}}).to_list(1)