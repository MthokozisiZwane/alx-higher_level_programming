#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
Safe from MySQL injections!
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Establishing a connection to the database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Creating a cursor object to interact with the database
    the_cursor = db.cursor()

    # Executing the SQL query with user input using parameterized query
    db_query = """
    SELECT cities.id, cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name=%s
    ORDER BY cities.id
    """
    the_cursor.execute(db_query, (sys.argv[4],))

    # Fetches all the rows and prints them
    rows = the_cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    the_cursor.close()
    db.close()
