from typing import List

from fastapi import APIRouter

from schemas.symptoms import SymptomListSchema, SymptomIdList
from services.symptoms import SymptomService

router = APIRouter()


@router.get("/symptoms/available")
async def get_available_symptoms() -> SymptomListSchema:
    return SymptomService.get_available_symptoms()


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
