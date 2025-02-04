from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column

from core.models import Base


class Patient(Base):
    __tablename__ = "Patient"  # Указываем имя таблицы
    id: Mapped[int] = mapped_column(primary_key=True)  # Явно говорим, что id - PK
    name: Mapped[str]
    surname: Mapped[str]
    patronymic: Mapped[str]
    phone: Mapped[str]
    home_address: Mapped[str]
    age: Mapped[int]
    gender_id: Mapped[int]
