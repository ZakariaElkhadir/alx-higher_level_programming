#!/usr/bin/python3

"""
This script connects 
to a MySQL database
"""


if __name__ == "__main__":
    import MySQLdb
    import sys

db_host = 'localhost'
db_user = sys.argv[1]
db_password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(
    host=db_host,
    user=db_user,
    passwd=db_password,
    db=database,
    port=3306)


cursor = db.cursor()


cursor.execute("SELECT * FROM states WHERE name \
LIKE BINARY 'N%' ORDER BY id ASC")

rows = cursor.fetchall()


for row in rows:
    print(row)


cursor.close()
db.close()
