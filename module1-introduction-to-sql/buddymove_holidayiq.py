import sqlite3
import pandas as pd
from rpg_queries import fetch_index

df = pd.read_csv("buddymove_holidayiq.csv")
df.to_sql('review', sqlite3.Connection("buddymove_holidayiq.sqlite3"))

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()
# Count how many rows you have - it should be 249!
rows = len(curs.execute('SELECT * FROM review').fetchall())
# How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?
num_users = len(curs.execute('SELECT "User Id" FROM review WHERE "Nature" > 99 AND "Shopping" > 99').fetchall())

print(f'Number of rows in review: {rows}')
print(f'Reviewers: {num_users}')

categories = ['Sports', 'Religious', 'Nature', 'Theatre', 'Shopping', 'Picnic']

for i in categories:
    print(f"""{i}'s avg reviews is: {fetch_index(f'SELECT avg("{i}") FROM review', curs)}""")
