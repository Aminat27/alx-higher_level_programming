#!/usr/bin/python3

"""
Ahmed Adebayo
This is the State module
This module handles  Base that inherits from declarative_Base module
"""

from model_state import Base
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """City class definition"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
