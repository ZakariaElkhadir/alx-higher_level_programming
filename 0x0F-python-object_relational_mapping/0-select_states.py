#!/usr/bin/python3
"""gets all states via python yee boi
"""


def main(args):
    """gets all state stuff
    """
    db = MySQLdb.connect(
        host='localhost',
        user=args[1],
        passwd=args[2],
        db=args[3])
    
    cur = db.cursor()
    
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    
    for state in states:
        print(state)


if __name__ == "__main__":
    import MySQLdb
    import sys
    main(sys.argv)
