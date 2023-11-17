#!/usr/bin/python3
"""
Script to list all states from a MySQL database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    the_cursor = db.cursor()

    the_cursor.execute("SELECT * FROM states ORDER BY id")

    results = the_cursor.fetchall()

    for row in results:
        print(row)

    the_cursor.close()
    db.close()
