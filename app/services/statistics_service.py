from app.repositories.stats_repo import StatisticsRepository

class StatisticsService:
    def __init__(self, stats_col):
        self.repo = StatisticsRepository(stats_col)

    async def get_user_stats(self, user_id: str):
        return await self.repo.get_user_stats(user_id)

    async def get_global_stats(self):
        return await self.repo.get_global_stats()