#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=database)
        cursor = conn.cursor()

        # Query to select all states from the states table
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows and display results
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # Close cursor and connection
        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
