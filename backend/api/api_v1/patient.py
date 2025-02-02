from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from core.schemas.patient import PatientRead, PatientCreate
from crud.patient import get_all_patient

router = APIRouter(
    prefix=settings.api.v1.patient,
    tags=["Patient"],
)

@router.get("/", response_model=list[PatientRead])
async def get_patient(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    patients = await get_all_patient(session=session)  # Использовать await здесь
    return patients


@router.get("/add")
async def render_patient_add():
    pass
'''
@router.post("/add", response_model=list[PatientCreate])
async def render_patient_add(
    session: AsyncSession = Depends(db_helper.session_getter),

):
    new_patient = PatientCreate(
        name=name
    )
    session.add(new_patient)
    session.commit()
'''