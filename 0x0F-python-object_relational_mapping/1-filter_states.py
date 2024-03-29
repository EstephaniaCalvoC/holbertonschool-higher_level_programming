#!/usr/bin/python3
"""
List all states with a name starting with N from the database hbtn_0e_0_usa.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    _user = argv[1]
    _pw = argv[2]
    _dbname = argv[3]

    conn = MySQLdb.connect(
         host="localhost",
         port=3306,
         user=_user,
         passwd=_pw,
         db=_dbname,
         charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for s in states:
        if s[1][0] == 'N':
            print(s)
    cur.close()
    conn.close()
