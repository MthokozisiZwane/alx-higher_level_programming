#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Creating an SQLAlchemy Engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Creating an SQLAlchemy ORM session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating a new State object
    new_state = State(name="Louisiana")

    # Adding the new State object to the session
    session.add(new_state)

    # Commiting the session to save the changes to the database
    session.commit()

    # Prints the id of the newly added State object
    print(new_state.id)

    # Closes the session
    session.close()
