from fastapi import APIRouter

from core.config import settings

from .patient import router as patient_router

router = APIRouter(
    prefix=settings.api.v1.prefix
)
router.include_router(
    patient_router,
)
