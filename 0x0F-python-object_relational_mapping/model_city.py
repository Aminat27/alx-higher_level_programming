#!/usr/bin/python3

"""
This is the State module
This module handles  Base that inherits from declarative_Base module
"""

from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """City class definition"""


    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
