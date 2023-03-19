#!/usr/bin/python3
"""A script that list all cities from the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
# Create a cursor object
    cursor = db.cursor()

# Define the query to select all states from the table
    query = """SELECT cities.id, cities.name, states.name FROM
            cities INNER JOIN states ON state.id=cities.state_id"""

# Execute the query
    cursor.execute(query)

# Fetch all the results
    results = cursor.fetchall()

# Print the list of states
    for row in results:
        print(row)

# Close the cursor and database connections
    cursor.close()
    db.close()
