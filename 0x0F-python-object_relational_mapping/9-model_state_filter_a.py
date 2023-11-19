#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a from the
database hbtn_0e_6_usa.
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

    # Query to get all State objects that contain 'a' in their name
    states_with_a =
    session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    # Prints the results or a message if no results found
    if states_with_a:
        for state in states_with_a:
            print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    # Closes the session
    session.close()
