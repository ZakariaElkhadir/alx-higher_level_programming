#!/usr/bin/python3

"""
This script connects to a MySQL database,
 executes a query to retrieve states
 whose names start with 'N',
 and prints the results.
"""

# Import required libraries
if __name__ == "__main__":
    import MySQLdb
    import sys

# Get command line arguments for database connection
db_host = 'localhost'
db_user = sys.argv[1]
db_password = sys.argv[2]
database = sys.argv[3]

# Connect to the MySQL database
db = MySQLdb.connect(
    host=db_host,
    user=db_user,
    passwd=db_password,
    db=database,
    port=3306)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Execute SQL query to select states whose names start with 'N'
cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%'")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the retrieved data
for row in rows:
    print(row)

# Close cursor and database connection
cursor.close()
db.close()
