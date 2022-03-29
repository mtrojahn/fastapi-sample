from application.database import get_db, SessionLocal

session = SessionLocal()
if session.bind.name != "sqlite":
    raise Exception("You are trying to run tests on a database other than sqlite")
