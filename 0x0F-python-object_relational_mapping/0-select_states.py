#!/usr/bin/python3
""" SELECT all data in the table states"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")

    for row in cur.fetchall():
        print (row)
    cur.close()
    db.close()
