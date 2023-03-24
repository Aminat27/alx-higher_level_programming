#!/usr/bin/python3

"""
inserts or add into the database a state
sunday moses
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(*argv[1:4]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()

    newState = State(name="Louisiana")
    session.add(newState)
    session.commit()

    print(newState.id)
    session.close()
