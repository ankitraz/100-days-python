# json - javascript object notation

# many popular websites provide their data in json format
# json is a lightweight data-interchange format
# json is language independent
# json is easy to read and write
# json is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. These properties make JSON an ideal data-interchange language.

import json
from pathlib import Path



movies = [
    {"id": 1, "title": "Terminator", "year": 1984},
    {"id": 2, "title": "Kindergarten Cop", "year": 1990},
    {"id": 3, "title": "Die Hard", "year": 1988},
]

data = json.dumps(movies)
print(data) # it will print an array of dictionaries


# to write this data to a file
# import pathlib form pathlib import Path

file = Path("movies.json").write_text(data)


# to read the data from the json file

file = Path("movies.json").read_text()
# we need to parse this string into json
movies = json.loads(file)
print(movies)

# we can also get the value of a key
print(movies[0]["title"])