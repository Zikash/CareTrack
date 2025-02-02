from fastapi import APIRouter

from core.config import settings

from .patient import router as patient_router
from .doctor import router as doctor_router

router = APIRouter(
    prefix=settings.api.v1.prefix
)
router.include_router(
    patient_router,
)
router.include_router(
    doctor_router,
)
