"""
FOR MY TL, remember for this to run you must delete titanic.sqlite3 and have a DB without a table named titanic,
also, the warning is because columns in the titanic df have spaces, also also, because there where only 9 instances
of words with ' i just deleted the ' but, i could make a function that would escape the ' for my df then when i pass it
into the DB there would be no issues
"""

import psycopg2
import pandas as pd
import sqlite3


def conn_curs():
    dbname = "gdhyqmwk"
    user = "gdhyqmwk"

    with open("password.txt", 'r') as file:
        password = file.read()

    host = "isilo.db.elephantsql.com"
    conn = psycopg2.connect(dbname=dbname, user=user,
                            password=password, host=host)
    curs = conn.cursor()
    return curs, conn


df = pd.read_csv('titanic.csv')
# length = 0
# name = ''
# for i in df.Name:
#     if len(i) > length:
#         name = i
#         length = len(i)
# print(length, name)

schema = """
CREATE TABLE titanic  (
  Index SERIAL PRIMARY KEY,
  Survived INT,
  Pclass INT,
  Name varchar(81) NOT NULL,
  Sex varchar(6) NOT NULL,
  Age FLOAT,
  "Siblings/Spouses Aboard" INT,
  "Parents/Children Aboard" INT,
  Fare FLOAT
)
"""  # for making table
#
# # makes table
curs, conn = conn_curs()
curs.execute(schema)
conn.commit()
# make data sql
df.to_sql('titanic', sqlite3.Connection("titanic.sqlite3"))
# new conn and curs for titanic
titanic_conn = sqlite3.connect('titanic.sqlite3')
titanic_curs = titanic_conn.cursor()
# Get data from titanic sql
get_char = "SELECT * FROM titanic"
titanic_curs.execute(get_char)
data = titanic_curs.fetchall()
# insert the data
for person in data:
    insert_character = f"""
    INSERT INTO titanic
    (Survived, Pclass, Name, Sex, Age, "Siblings/Spouses Aboard","Parents/Children Aboard", Fare)
    VALUES {person[1:]};"""
    curs.execute(insert_character)
    # save the data
    conn.commit()
