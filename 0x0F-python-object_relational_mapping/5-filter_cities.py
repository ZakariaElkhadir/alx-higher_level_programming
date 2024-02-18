#!/usr/bin/python3


def main(argument):
    db = MySQLdb.connect(
        host='localhost',
        user=argument[1],
        passwd=argument[2],
        db=argument[3] 
        )
    cursor = db.cursor()

    query = (
        "SELECT c.name "
        "FROM cities c "
        "JOIN states s ON s.id = c.state_id "
        "WHERE s.name = %s "
        "ORDER BY c.id ASC"
    )
    cursor.execute(query, (argument[4],))
    states = cursor.fetchall()
    
    """Join the states with commas and spaces using map and lambda"""
    comma_seperated_states = ", ".join(map(lambda x: "%s" % x, states))
    print(comma_seperated_states)
                  
    
if __name__ == "__main__":
    import MySQLdb
    import sys
    main(sys.argv)