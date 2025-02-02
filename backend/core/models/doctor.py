from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class Doctor(Base):
    __tablename__ = "Doctor"

    id: Mapped[int] = mapped_column(primary_key=True)  # Явно говорим, что id - PK
    name: Mapped[str]
    surname: Mapped[str]
    patronymic: Mapped[str]
    phone: Mapped[str]
    serviced_area_number: Mapped[int]
    experience: Mapped[int]
