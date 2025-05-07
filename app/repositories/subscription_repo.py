class SubscriptionRepository:
    def __init__(self, collection):
        self.col = collection

    async def start_subscription(self, user_id: str, start_date: str):
        return await self.col.insert_one({
            "user_id": user_id,
            "start_date": start_date,
            "active": True
        })

    async def cancel_subscription(self, user_id: str):
        return await self.col.update_one(
            {"user_id": user_id, "active": True},
            {"$set": {"active": False}}
        )
