#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Creates an SQLAlchemy Engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Creates an SQLAlchemy ORM session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get all State objects
    all_states = session.query(State).order_by(State.id).all()

    # Prints the results or a message if no results found
    if all_states:
        for state in all_states:
            print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    # Closes the session
    session.close()
