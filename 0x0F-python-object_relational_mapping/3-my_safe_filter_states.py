#!/usr/bin/python3
''' SELECT all data in the table
    states with first leter is N'''

if __name__ == '__main__':
    import sys
    import MySQLdb

    name = (sys.argv[4],)
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    cur = db.cursor()

    cur.execute(("SELECT * FROM states "
                    "WHERE name=%s "
                    "ORDER BY id"), name)
    for row in cur.fetchall():
        print (row)
    cur.close()
    db.close()
