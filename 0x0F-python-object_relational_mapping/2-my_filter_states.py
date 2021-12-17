#!/usr/bin/python3
"""
return all table thtat looks like user input
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
    c.execute("""SELECT * FROM states WHERE name LIKE {:s} ORDER BY id ASC""".format(argv[4]))
    for row in c.fetchall():
        print(row)
    c.close()
    db.close()
