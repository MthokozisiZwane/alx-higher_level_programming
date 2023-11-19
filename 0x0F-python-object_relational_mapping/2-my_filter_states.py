#!/usr/bin/python3

"""
Script to display states based on user input from MySQL database
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
    # Creating a cursor object
    the_cursor = db.cursor()

    # Execute the SQL query with user input
    the_cursor.execute("SELECT * FROM states WHERE
                       name=%s ORDER BY id", (sys.argv[4],))

    # Fetching the results
    results = the_cursor.fetchall()

    # Displaying the results
    for row in results:
        print(row)

    # Closing the database connection
    the_cursor.close()
    db.close()
