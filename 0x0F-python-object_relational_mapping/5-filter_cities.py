#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3])
    cur = db.cursor()
    cur.execute(
        """SELECT cities.name FROM
        cities INNER JOIN states ON states.id=cities.state_id
        WHERE states.name=%s""", (sys.argv[4],))
    rows = cur.fetchall()
    for state in rows:
        if state != rows[len(rows) - 1]:
            print(f"{state[0]}, ", end="")
        else:
            print(state[0])
    cur.close()
    db.close()
