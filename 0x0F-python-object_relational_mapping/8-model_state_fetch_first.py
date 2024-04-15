#!/usr/bin/python3
"""
This script prints the first `State` object
from the database `hbtn_0e_6_usa`.
Usage: ./8-model_state_fetch_first.py <mysql username>
        <mysql password> <database name>
"""

import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import (sessionmaker)

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    state = session.query(State).order_by(State.id).first()
    if state is not None:
        print('{}: {}'.format(state.id, state.name))
    else:
        print("Nothing")
