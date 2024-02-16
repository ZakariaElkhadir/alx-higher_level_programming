#!/usr/bin/python3
if __name__ == "__main__":
    import MySQLdb
    import sys

    # Get arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to fetch states, ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and display the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
