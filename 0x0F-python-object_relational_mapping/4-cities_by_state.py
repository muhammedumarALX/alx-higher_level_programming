#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_us"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT c.id, c.name, s.name FROM cities AS c\
            INNER JOIN states AS s\
            ON c.state_id = s.id"
    cur.execute(query)
    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    db.close()
