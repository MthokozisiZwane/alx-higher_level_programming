#!/usr/bin/python3
"""
Script to list states starting with the letter 'N' from MySQL database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connection to the database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    # Creation of a a cursor object
    the_cursor = db.cursor()

    # Executing the SQL query to get states starting with 'N'
    the_cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    # Fetching all the results starting with N
    results = the_cursor.fetchall()

    # Displaying the results
    for row in results:
        print(row)

    # Closes the database connection
    the_cursor.close()
    db.close()
