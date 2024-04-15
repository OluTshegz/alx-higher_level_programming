#!/usr/bin/python3
"""
This script deletes all `State` objects with a name containing
the letter `a` from the database `hbtn_0e_6_usa`.
"""

import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import (sessionmaker)

if __name__ == "__main__":
    """
    Deletes State objects on the database.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    states = session.query(State).filter(State.name.like('%a%')).all()
    if states is not None:
        for state in states:
            session.delete(state)

    session.commit()
    session.close()
