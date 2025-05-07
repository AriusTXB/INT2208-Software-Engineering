from fastapi import APIRouter, Depends
from app.services.registration_service import RegistrationService
from app.databases.mongodb import get_user_collection

router = APIRouter()

@router.post("/register")
async def register(data: dict, user_col=Depends(get_user_collection)):
    return await RegistrationService(user_col).register_user(data)