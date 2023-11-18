#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Creates an SQLAlchemy Engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Creates an SQLAlchemy ORM session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieves all State objects with a name containing the letter 'a'
    states_to_delete =
    session.query(State).filter(State.name.like('%a%')).all()

    # Deletes the selected State objects
    for state in states_to_delete:
        session.delete(state)

    # Commits the session to save the changes to the database
    session.commit()

    # Closes the session
    session.close()
