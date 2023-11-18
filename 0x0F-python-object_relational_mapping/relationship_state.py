from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_base import Base


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Establishing a relationship with the City class
    cities =
    relationship("City", back_populates="state", cascade="all, delete-orphan")
