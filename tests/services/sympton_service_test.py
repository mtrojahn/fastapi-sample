from fastapi.testclient import TestClient

from application.app import create_app
from application.database import Base, SessionLocal, engine
from tests import testdata

"""
A few reminders:
The database decision is bound to the existence of the DATABASE_DSN environment variable. If the variable is not set,
the SQLite database is used, otherwise, the DATABASE_DSN is used. 

TESTS SHOULD NEVER BE RUN IN PRODUCTION. 
"""

app = create_app()
client = TestClient(app)
session = SessionLocal()


# runs before each test to recreate tables. they are in-memory, so they are not persistent
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
