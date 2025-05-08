from app.repositories.subscription_repository import SubscriptionRepository
from datetime import datetime

class SubscriptionService:
    def __init__(self, sub_col):
        self.repo = SubscriptionRepository(sub_col)

    async def start_subscription(self, user_id: str):
        return await self.repo.start_subscription(user_id, datetime.utcnow().isoformat())

    async def cancel_subscription(self, user_id: str):
        return await self.repo.cancel_subscription(user_id)