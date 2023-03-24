#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa using SQLAlchemy module.
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

    state = session.query(State).filter(State.name == (argv[4], )).first()
    if state is None:
        print("Not found")
    print("{}".format(state.id))
