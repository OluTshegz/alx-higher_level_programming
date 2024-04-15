#!/usr/bin/python3
"""
This script prints the first `State` object
from the database `hbtn_0e_6_usa`.
"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get a state id
    from the database.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    state = session.query(State).filter(State.name == argv[4]).first()
    if state is not None:
        print('{}'.format(state.id))
    else:
        print("Not found")
