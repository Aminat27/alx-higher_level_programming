#!/usr/bin/python3
"""List all states from the database in ascending order of states"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
# Create a cursor object
    cursor = db.cursor()

# Define the query to select all states from the table
    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))

# Fetch all the results
    results = cursor.fetchall()

# Print the list of states
    res = list(row[0] for row in results)
    print(*res, sep=", ")

# Close the cursor and database connections
    cursor.close()
    db.close()
