#!/usr/bin/python3


def main(args):
    db = MySQLdb.connect(host='localhost', user=args[1], passwd=args[2], db=args[3])

    cursor = db.cursor()

    query = (
        "SELECT * FROM states "
        "WHERE name LIKE BINARY '{}%' "
        "ORDER BY id ASC"
    ).format(args[4])
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

if __name__ == "__main__":
    import MySQLdb
    import sys
    main(sys.argv)
