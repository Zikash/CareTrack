from typing import Optional

from pydantic import BaseModel


class DoctorBase(BaseModel):
    name: str
    surname: str
    patronymic: Optional[str]
    phone: str
    serviced_area_number: int
    experience: Optional[int]

class DoctorCreate(DoctorBase):
    name: str
    surname: str
    patronymic: Optional[str]
    phone: str
    serviced_area_number: int
    experience: Optional[int]

class DoctorRead(DoctorBase):
    id: int