from fastapi import APIRouter, Depends
from app.services.account_service import AccountService
from app.databases.mongodb import get_user_collection

router = APIRouter()

@router.get("/account/profile")
async def get_profile(user_id: str, user_col=Depends(get_user_collection)):
    return await AccountService(user_col).get_user_profile(user_id)

@router.put("/account/profile")
async def update_profile(user_id: str, data: dict, user_col=Depends(get_user_collection)):
    return await AccountService(user_col).update_user_profile(user_id, data)
