#!/usr/bin/python3
''' SELECT all data in the table cities'''

if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities JOIN states "
                   "ON states.id = cities.state_id "
                   "ORDER BY cities.id ASC")
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()
