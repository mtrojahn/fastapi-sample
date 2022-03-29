import uuid

from faker import Faker
from sqlalchemy.orm import Session

from models.symptoms import Symptom

fake = Faker()


def create_symptom(session: Session, **kwargs) -> Symptom:
    props = {
        "id": str(uuid.uuid4()),
        "name": fake.name()
    }
    props.update(kwargs)

    symptom = Symptom(**props)
    session.add(symptom)
    session.commit()
    return symptom
