#!/usr/bin/python3


"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print('Nothing')
    print("{}: {}".format(state.id, state.name))
