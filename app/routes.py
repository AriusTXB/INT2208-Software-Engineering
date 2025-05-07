from fastapi import APIRouter
from app.controllers import (
    account_controller, account_delete_controller,
    premium_article_controller, premium_subscription_controller,
    read_news_controller, recommendations_controller,
    reg_controller, statistic_controller
)

router = APIRouter()

router.include_router(account_controller.router, prefix="/account")
router.include_router(account_delete_controller.router, prefix="/account")
router.include_router(premium_article_controller.router, prefix="/premium")
router.include_router(premium_subscription_controller.router, prefix="/subscription")
router.include_router(read_news_controller.router, prefix="/news")
router.include_router(recommendations_controller.router, prefix="/news")
router.include_router(reg_controller.router, prefix="/auth")
router.include_router(statistic_controller.router, prefix="/stats")