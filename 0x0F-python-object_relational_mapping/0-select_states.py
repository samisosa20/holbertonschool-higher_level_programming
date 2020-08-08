#!/usr/bin/python3
''' SELECT all data in the table states'''

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

    # Use all the SQL you like
    cur.execute("SELECT * FROM states ORDER BY id")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        print (row)
    cur.close()
    db.close()
