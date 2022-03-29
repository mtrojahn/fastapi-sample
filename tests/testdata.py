import uuid

from sqlalchemy.orm import Session

from models.symptoms import Symptom


def create_symptom(session: Session) -> Symptom:
    new_id = str(uuid.uuid4())
    symptom = Symptom(name="test_symptom", id=new_id)
    session.add(symptom)
    session.commit()
    return symptom
