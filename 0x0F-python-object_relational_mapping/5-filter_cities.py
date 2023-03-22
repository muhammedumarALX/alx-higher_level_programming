#!/usr/bin/python3
"""script that takes in the name of a state as an
    argument and lists all cities of that state,
    using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], user=sys.argv[2], user=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities as c\
                 INNER JOIN states as s\
                 ON c.statea-id = s.id\
                 WHERE s.name = %s", (sys.argv[4],))
    cities = cur.fetchall()

    print(', '.join([city[1} FOR city in cities]))

    cur.close()
    db.close()
