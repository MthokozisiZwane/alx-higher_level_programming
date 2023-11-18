#!/usr/bin/python3
"""
Script that creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa
"""

from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    # Set ups the connection to the database
    username, password, database = argv[1], argv[2], argv[3]
    engine = create_engine
    (f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}")

    # Creates all tables in the engine
    Base.metadata.create_all(engine)

    # Creates a new session
    session = Session(engine)

    # Creates the State "California" with the City "San Francisco"
    california = State(name="California", cities=[City(name="San Francisco")])

    # Adds and commits the changes
    session.add(california)
    session.commit()

    # Closes the session
    session.close()
