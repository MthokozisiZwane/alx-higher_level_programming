#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. Safe from MySQL injections!
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # connection to the database
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
    db_query = "SELECT * FROM states WHERE name=%s ORDER BY id"
    the_cursor.execute(db_query, (sys.argv[4],))

    # Fetching all the rows and print them
    rows = the_cursor.fetchall()
    for row in rows:
        print(row)

    # Closing the cursor and connection
    the_cursor.close()
    db.close()
