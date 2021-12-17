#!/usr/bin/python3
"""
return all table values (table 'states')
parameters given to script: username, password, database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # create cursor to exec queries using SQL
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    for row in c.fetchall():
        print(row)
    c.close()
    db.close()
