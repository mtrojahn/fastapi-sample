from sqlalchemy import JSON, Column, String

from application.database import Base


class User(Base):
    __tablename__ = "user_users"
    id = Column(String(36), primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    selected_symptoms = Column(JSON)
