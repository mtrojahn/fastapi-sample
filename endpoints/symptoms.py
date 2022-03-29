from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from application.database import get_db
from schemas.symptoms import SymptomIdList, SymptomListSchema, SymptomSchema
from services.symptoms import SymptomService

router = APIRouter()


@router.get("/symptoms/available", response_model=List[SymptomSchema])
async def get_available_symptoms(db: Session = Depends(get_db)):
    return SymptomService.get_available_symptoms(db)


@router.post("/symptoms/set_tracked_symptoms")
async def set_tracked_symptoms(symptoms: List[SymptomIdList]) -> SymptomListSchema:
    # TODO: get user_id from token
    user_id = "foo"
    return SymptomService.set_tracked_symptoms(user_id, symptoms)


@router.get("/symptoms/get_tracked_symptoms")
async def get_tracked_symptoms() -> SymptomListSchema:
    # TODO: get user_id from token
    user_id = "foo"
    return SymptomService.get_tracked_symptoms(user_id)
