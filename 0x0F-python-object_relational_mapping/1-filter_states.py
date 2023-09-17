#!/usr/bin/python3
""" lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
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
    cur.execute("SELECT * FROM `states` WHERE name LIKE BINARY 'N%';")
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
