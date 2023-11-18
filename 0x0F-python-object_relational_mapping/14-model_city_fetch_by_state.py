#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_14_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State
import sys

if __name__ == "__main__":
    # Creates an SQLAlchemy Engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Creates an SQLAlchemy ORM session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to retrieve all City objects
    cities = session.query(City).all()

    # Prints the cities with their corresponding state
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    # Close the session
    session.close()
