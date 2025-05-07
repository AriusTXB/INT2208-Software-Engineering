from app.repositories.user_repo import UserRepository

class AccountService:
    def __init__(self, user_col):
        self.repo = UserRepository(user_col)

    async def get_user_profile(self, user_id: str):
        return await self.repo.get_by_id(user_id)

    async def update_user_profile(self, user_id: str, data: dict):
        return await self.repo.update_profile(user_id, data)