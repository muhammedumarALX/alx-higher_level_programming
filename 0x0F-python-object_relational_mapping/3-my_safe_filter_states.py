#!/usr/bin/python3
"""write a script that takes in arguments"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE BINARY name =%s"
    cur.execute(query, (sys.argv[4],))

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
