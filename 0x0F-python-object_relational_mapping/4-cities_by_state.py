#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the cities table
of hbtn_0e_4_usa where name matches the argument.
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
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE cities.name=%s
    ORDER BY cities.id
    """
    the_cursor.execute(query, (sys.argv[4],))

    # Fetching all the rows and print them
    rows = the_cursor.fetchall()
    for row in rows:
        print(row)

    # Closes the cursor and connection
    the_cursor.close()
    db.close()
