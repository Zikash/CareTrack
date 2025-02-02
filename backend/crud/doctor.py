from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Doctor


async def get_all_doctor(session: AsyncSession):
    stmt = select(Doctor).order_by(Doctor.id)
    result = await session.scalars(stmt)
    return result.all()