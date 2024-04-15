#!/usr/bin/python3
"""
This script defines a model: `City` class definition and
an inherited `Base` class to work with `MySQLAlchemy` ORM.
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """`City` class inherits `Base` links MySQL table `cities`

    Attributes:
        __tablename__ (str): The table name of the class (private)
        id (int): The id of the class (public)
        name (str): The name of the class (public)
        state_id (int): The state the city belongs to
        Foreign-Key Relationship to/of id attribute of State class
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
