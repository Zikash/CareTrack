from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Patient


async def get_all_patient(session: AsyncSession):
    stmt = select(Patient).order_by(Patient.id)
    result = await session.scalars(stmt)
    return result.all()