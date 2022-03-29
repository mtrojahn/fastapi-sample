from typing import List

from pydantic import BaseModel


class SymptomId(BaseModel):
    id: str


class SymptomIdList(BaseModel):
    id: List[SymptomId]


class SymptomSchema(BaseModel):
    name: str
    description: str
    severity: str
    category: str

    class Config:
        orm_mode = True


class SymptomListSchema(BaseModel):
    symptoms: List[SymptomSchema]


class SymptomLogSchema(BaseModel):
    symptom_id: int
    user_id: int
    date: str
    time: str
    severity: str
    category: str

    class Config:
        orm_mode = True
