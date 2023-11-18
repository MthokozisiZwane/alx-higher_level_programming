#!/usr/bin/python3
"""
Script that lists all State objects and corresponding City objects
contained in the database hbtn_0e_101_usa
"""

from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    # Sets up the connection to the database
    username, password, database = argv[1], argv[2], argv[3]
    engine = create_engine
    (f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}")

    # Creates all tables in the engine
    Base.metadata.create_all(engine)

    # Creates a new session
    session = Session(engine)

    # Query and print State and City objects
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    # Closes the session
    session.close()
