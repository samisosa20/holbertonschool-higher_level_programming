#!/usr/bin/python3
''' SELECT all data in the table
    states with first leter is N'''

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

    # you must create a Cursor object. It will let
    #  you execute all the queries you need

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' \
        ORDER BY id".format(sys.argv[4])

    # Use all the SQL you like
    cur.execute(query)
    # print all the first cell of all the rows
    for row in cur.fetchall():
        print (row)
    cur.close()
    db.close()
