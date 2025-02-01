from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.schemas.patient import PatientRead
from crud.patient import get_all_patient

router = APIRouter(
    tags=["Patient"],
)

@router.get("/", response_model=list[PatientRead])
async def get_patient(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    patients = await get_all_patient(session=session)  # Использовать await здесь
    return patients