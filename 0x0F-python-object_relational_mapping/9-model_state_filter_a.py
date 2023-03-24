#!/usr/bin/python3
"""
prints all states that contain the lettter 'a'
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(*argv[1:4]))

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()

    states = session.query(State).filter(State.name.like('%a%'))

    for state in states:
        print("{}: {}".format(state.id, state.name))
