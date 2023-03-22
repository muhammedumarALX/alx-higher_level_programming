#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_us"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities as c\
                 inner join states as s\
                 ON c.state_id = s.id")
    cities = cur.fetchall()

    for city in cities:
        print(ctiy)

    cur.close()
    db.close()
