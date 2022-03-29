from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship

from application.database import Base


class Symptom(Base):
    __tablename__ = "symptoms"
    id = Column(String(36), primary_key=True, index=True)
    name = Column(String(50), nullable=False)


class SymptomLog(Base):
    __tablename__ = "symptom_logs"
    id = Column(String(36), primary_key=True, index=True)
    symptom_id = Column(String(36), nullable=False)
    user_id = Column(String(36), nullable=False)
    severity = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)

    symptom = relationship("Symptom")
    user = relationship("User")
