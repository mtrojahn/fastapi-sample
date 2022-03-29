import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

DATABASE_DSN = os.environ.get("DATABASE_DSN") or "sqlite://"
if DATABASE_DSN.startswith("sqlite"):
    args = {"check_same_thread": False}
    engine = create_engine(DATABASE_DSN, echo=True, poolclass=StaticPool, connect_args=args)
else:
    engine = create_engine(DATABASE_DSN)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    connection = engine.connect()
    connection.begin()
    db = SessionLocal(bind=connection)
    try:
        yield db
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()
        db.close()

