from typing import Optional

from pydantic import BaseModel


class PatientBase(BaseModel):
    name: str
    surname: str
    patronymic: Optional[str]
    phone: str
    home_address: str
    age: int
    gender_id: int

class PatientCreate(PatientBase):
    pass

class PatientRead(PatientBase):
    id: int
