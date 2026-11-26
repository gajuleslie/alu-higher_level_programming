#!/usr/bin/python3
"""List all cities of a state safely from the hbtn_0e_4_usa database."""

import sys

import MySQLdb


if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=sys.argv[1], passwd=sys.argv[2],
                                 db=sys.argv[3], charset="utf8")
    cursor = connection.cursor()
    query = ("SELECT cities.name FROM cities "
             "INNER JOIN states ON cities.state_id = states.id "
             "WHERE BINARY states.name = %s ORDER BY cities.id ASC")
    cursor.execute(query, (sys.argv[4],))
    cities = [row[0] for row in cursor.fetchall()]
    print(", ".join(cities))
    cursor.close()
    connection.close()
