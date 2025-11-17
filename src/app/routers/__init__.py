__all__ = ("router",)

from fastapi import APIRouter

from app.routers.api import router as api_router

router = APIRouter()
router.include_router(api_router)
