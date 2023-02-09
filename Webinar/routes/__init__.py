from fastapi import APIRouter
from .ID import router as include_router

router = APIRouter()
router.include_router(include_router)