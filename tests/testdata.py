import uuid

from faker import Faker
from sqlalchemy.orm import Session

from models.symptoms import Symptom

fake = Faker()


def create_symptom(session: Session, **kwargs) -> Symptom:
    defaults = {"id": str(uuid.uuid4()), "name": fake.name()}
    symptom = Symptom(**{**defaults, **kwargs})
    session.add(symptom)
    session.flush()
    return symptom
