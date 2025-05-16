#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    # Create cursor object to interact with the database
    cursor = db.cursor()

    # Execute SQL query to retrieve all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print all results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
