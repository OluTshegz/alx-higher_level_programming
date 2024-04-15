#!/usr/bin/python3
"""
Lists all `State` objects and corresponding `City`
objects in the database `hbtn_0e_101_usa`.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """
    Access to the database and get the `states`
    and its corresponding `cities`from the database.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    cities_states = session.query(State).\
        outerjoin(City).order_by(State.id, City.id).all()

    for state in cities_states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
