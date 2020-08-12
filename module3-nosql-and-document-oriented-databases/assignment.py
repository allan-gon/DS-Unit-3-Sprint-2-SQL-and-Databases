import pymongo
import sqlite3
import psycopg2


"""DONT WORRY, I RESET THE PASSWORD ON MY END"""
# connect to mongo db
passw = "RxgkqRbRJlK7yw1F"
dbname = 'rpg'
connection = ("mongodb+srv://diz8nBMbcD1RjaYE:" + passw +
              "@mod3.gn8np.mongodb.net/" + dbname +
              "?retryWrites=true&w=majority")
client = pymongo.MongoClient(connection)
db = client.test


def conn_curs():
    dbname = "gdhyqmwk"
    user = "gdhyqmwk"

    with open("../module2-sql-for-analysis/password.txt", 'r') as file:
        password = file.read()

    host = "isilo.db.elephantsql.com"
    conn = psycopg2.connect(dbname=dbname, user=user,
                            password=password, host=host)
    curs = conn.cursor()
    return curs, conn


# connect to sqlite
curs, conn = conn_curs()

# get character data
get_char = "SELECT * FROM charactercreator_character"
curs.execute(get_char)
characters = curs.fetchall()

# deleting so you can run it
db.rpg.remove()

# insert dta into mongo db
for character in characters:
    key = character[1].replace('.', '')
    value = character[2:]
    db.rpg.insert_one({key: value})

# proof that it's there
print(list(db.rpg.find()))

# Q - How was working with MongoDB different from working with PostgreSQL?
# A - Different to access, simpler i think. Can't just see my tables
# What was easier, and what was harder?
# A - They were about the same but sql was probably simper because i can actually see
# my tables
