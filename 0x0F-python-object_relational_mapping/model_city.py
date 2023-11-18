from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_base import Base


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Establishing a relationship with the State class
    state = relationship("State", back_populates="cities")
