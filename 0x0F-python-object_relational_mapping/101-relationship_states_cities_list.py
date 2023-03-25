#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City


if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Connect to MySQL server using SQLAlchemy
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database for all State objects and their corresponding City objects
    st = session.query(State).outerjoin(City).order_by(State.id, City.id).all()
    for state in st:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    # Clean up
    session.close()
    sys.exit(0)
