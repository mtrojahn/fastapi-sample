import datetime

from sqlalchemy.orm import Session

from models.symptoms import Symptom


class SymptomService:
    @classmethod
    def get_available_symptoms(cls, db: Session):
        return db.query(Symptom).all()

    @classmethod
    def get_selected_symptoms(cls, user_id: str):
        pass

    @classmethod
    def set_tracked_symptoms(cls, user_id: str, symptoms: list):
        pass

    @classmethod
    def created_tracked_symptoms_entry(cls, user_id: str, symptom: Symptom, severity: int, date: datetime.date):
        pass

    @classmethod
    def get_tracked_symptoms(cls, user_id: str):
        pass
