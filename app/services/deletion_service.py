from app.repositories.user_repo import UserRepository

class DeletionService:
    def __init__(self, user_col):
        self.repo = UserRepository(user_col)

    async def delete_user(self, user_id: str):
        return await self.repo.delete_user(user_id)