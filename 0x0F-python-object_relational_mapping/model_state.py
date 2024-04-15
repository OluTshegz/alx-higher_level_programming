#!/usr/bin/python3
"""
This script defines a model: `State` class definition and
an inherited `Base` class to work with `MySQLAlchemy` ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """`State` class inherits `Base` links MySQL table `states`

    Attributes:
        __tablename__ (str): The table name of the class (private)
        id (int): The State id of the class (public)
        name (str): The State name of the class (public)
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
