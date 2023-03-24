#!/usr/bin/python3
""" prints the State Louisiana
    with the name passed as argument from the database
"""
import sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# create new State object
new_state = State(name='Louisiana')

# add new_state to session and commit changes
session.add(new_state)
session.commit()

print(new_state.id)
session.cllose()
