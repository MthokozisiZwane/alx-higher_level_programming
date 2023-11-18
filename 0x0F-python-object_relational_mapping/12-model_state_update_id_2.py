#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Createing an SQLAlchemy Engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Creating an SQLAlchemy ORM session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieves the State object with id=2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Updates the name of the State object
    state_to_update.name = "New Mexico"

    # Commiting the session to save the changes to the database
    session.commit()

    # Closes the session
    session.close()
