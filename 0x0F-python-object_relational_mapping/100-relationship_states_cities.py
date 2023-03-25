#!/usr/bin/python3
"""
Script that creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa using SQLAlchemy
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    # Arguments validation
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Engine creation
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Session creation and State creation
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()
    session.close()
