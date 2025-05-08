from app.repositories.user_repository import UserRepository
from app.utils.password_hasher import hash_password

class RegistrationService:
    def __init__(self, user_col):
        self.repo = UserRepository(user_col)

    async def register_user(self, data: dict):
        data["hashed_password"] = hash_password(data.pop("password"))
        return await self.repo.col.insert_one(data)