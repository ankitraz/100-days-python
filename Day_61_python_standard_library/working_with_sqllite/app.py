# SQLite database is a lightweight database that is used for small applications
# it allows us to store data in a form of tables 

import sqlite3


# lets read some data from json file and store them in sqlite database
# we will use json module to read data from json file

import json
from pathlib import Path


# movies = json.loads(Path("movies.json").read_text())
# print(movies)
# we get list of dictionaries and now we want to store this list in database


# with sqlite3.connect("db.sqlite3") as connection:  # this will create a database file in our current directory
# # if db.sqlite3 file already exists then it will connect to that file and not then create a new one
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"  # this is a query to insert data into Movies table
# # we have 3 columns in Movies table so we need to pass 3 values in query
# # we will use ? as placeholders for values and then we will pass values as a tuple

#     for movie in movies:
#         connection.execute(command, tuple(movie.values()))
#     connection.commit()  # this will save the changes to database



# read data from database
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"  # this will select all the data from Movies table
    cursor = conn.execute(command) # this will execute the query and return a cursor object, A cursor is a control structure that enables traversal over the records in a database
    # for row in cursor:
    #     print(row)
    # conn.commit() # we don't need to commit changes when we are reading data from database

    print(cursor.fetchall())  # this will return all the rows from the cursor object

