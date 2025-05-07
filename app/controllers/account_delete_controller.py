from fastapi import APIRouter, Depends
from app.services.deletion_service import DeletionService
from app.databases.mongodb import get_user_collection

router = APIRouter()

@router.delete("/account/delete")
async def delete_account(user_id: str, user_col=Depends(get_user_collection)):
    return await DeletionService(user_col).delete_user(user_id)
