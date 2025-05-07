from fastapi import APIRouter, Depends
from app.services.subscription_service import SubscriptionService
from app.databases.mongodb import get_subscription_collection

router = APIRouter()

@router.post("/subscription/start")
async def start_subscription(user_id: str, sub_col=Depends(get_subscription_collection)):
    return await SubscriptionService(sub_col).start_subscription(user_id)

@router.post("/subscription/cancel")
async def cancel_subscription(user_id: str, sub_col=Depends(get_subscription_collection)):
    return await SubscriptionService(sub_col).cancel_subscription(user_id)