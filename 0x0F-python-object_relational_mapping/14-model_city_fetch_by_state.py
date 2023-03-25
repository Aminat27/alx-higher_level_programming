#!/usr/bin/python3
"""
Adebayo Ahmed
Prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City)\
            .filter(State.id == City.state_id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
