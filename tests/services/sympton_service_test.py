from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from application.app import create_app
from application.database import Base, SessionLocal, engine
from tests import testdata

app = create_app()
client = TestClient(app)
session: Session = SessionLocal()


def setup_module():
    Base.metadata.create_all(bind=engine)


def test_get_available_symptoms():
    symptom = testdata.create_symptom(session)

    response = client.get("/symptoms/available")
    assert response.status_code == 200
    result = response.json()
    assert len(result) == 1
    assert result[0]["name"] == symptom.name
    assert result[0]["id"] == symptom.id
