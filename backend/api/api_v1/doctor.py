from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from core.schemas.doctor import DoctorRead
from crud.doctor import get_all_doctor

router = APIRouter(
    prefix=settings.api.v1.doctor,
    tags=["Doctor"],
)

@router.get("/", response_model=list[DoctorRead])
async def get_doctor(
    session: AsyncSession = Depends(db_helper.session_getter)
):
    doctors = await get_all_doctor(session=session)
    return doctors