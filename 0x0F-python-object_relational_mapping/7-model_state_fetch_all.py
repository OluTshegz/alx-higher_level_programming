#!/usr/bin/python3
"""
This script lists all `State` objects
from the database `hbtn_0e_6_usa`.
Usage: ./7-model_state_fetch_all.py <mysql username>
        <mysql password> <database name>
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
