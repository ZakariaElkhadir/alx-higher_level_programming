#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""


def main(args):
    """gets all state
    """
    db = MySQLdb.connect(
        host='localhost',
        user=args[1],
        passwd=args[2],
        db=args[3])
    cur = db.cursor()
    query = (
        "SELECT cities.id, cities.name, states.name FROM cities "
        "JOIN states ON states.id = cities.state_id "
        "ORDER BY cities.id"
    )
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    import MySQLdb
    import sys
    main(sys.argv)
