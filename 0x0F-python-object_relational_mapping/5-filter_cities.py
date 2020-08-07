#!/usr/bin/python3
''' SELECT all data in the table cities'''

if __name__ == '__main__':
    import sys
    import MySQLdb

    state = (sys.argv[4],)
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute(("SELECT cities.id, cities.name FROM cities \
    JOIN states ON (states.id = cities.state_id) \
    WHERE states.name = %s ORDER BY cities.id"), state)

    # print all the first cell of all the rows
    for row in cur.fetchall():
        print (row[1])
    cur.close()
    db.close()
