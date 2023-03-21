#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa
with name starting with N (upper N)"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    state = cursor.execute("SELECT * FROM states WHERE BINARY name LIkE 'N%'")
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
