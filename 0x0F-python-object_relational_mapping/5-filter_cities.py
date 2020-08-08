#!/usr/bin/python3
''' SELECT all data in the table cities'''

if __name__ == '__main__':
    import sys
    import MySQLdb

    state = (sys.argv[4],)
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    cursor.execute(("SELECT cities.id, cities.name \
                FROM states JOIN cities \
                ON states.id = cities.state_id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC"), state)
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()
