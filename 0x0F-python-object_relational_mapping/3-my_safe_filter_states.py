#!/usr/bin/python3
"""
script that takes in arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
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
        "SELECT * FROM `states` WHERE BINARY name=%s;",
        (sys.argv[4],))
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
