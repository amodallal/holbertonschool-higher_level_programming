#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
Uses the module MySQLdb to connect to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        # Connect to the database
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=db_name)

        # Create a cursor object
        cursor = db.cursor()

        # Execute the SQL query
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows
        rows = cursor.fetchall()

        # Print the rows
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close the cursor and database connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'db' in locals() and db is not None:
            db.close()
