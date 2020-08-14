import pymongo
import psycopg2

# connecting to database MONGODB
"""DONT WORRY, I RESET THE PASSWORD ON MY END"""
# connect to mongo db
password = "OmnfnZvAb4Sm6Qfb"
dbname = 'rpg'
connection = ("mongodb+srv://diz8nBMbcD1RjaYE:" + password +
              "@mod3.gn8np.mongodb.net/" + dbname +
              "?retryWrites=true&w=majority")
client = pymongo.MongoClient(connection)
db = client.test

# checking that everything is there
characters = list(db.rpg.find())


# Questions
# How many total Characters are there?
print(f"There are {len(characters)} total  characters.")
# How many of each specific subclass?
necro = list(db.rpg.find({'subclass': 'necromancer'}))
print(f"There are {len(necro)} necromancers")
mages = list(db.rpg.find({'subclass': 'mage'}))
print(f"There are {len(mages) + len(necro)} mages")
thieves = list(db.rpg.find({'subclass': 'thief'}))
print(f"There are {len(thieves)} thieves")
clerics = list(db.rpg.find({'subclass': 'cleric'}))
print(f"There are {len(clerics)} clerics")
fighters = list(db.rpg.find({'subclass': 'fighter'}))
print(f"There are {len(fighters)} fighters")
# How many total Items?
num_item = set()
for character in characters:
    temp = character['inv']
    for item in temp:
        num_item.add(item)
print(f"There are {len(num_item)} items")
# How many of the Items are weapons? How many are not?
print(f"There are {characters[0]['tot_num_weapons']} weapons")
print(f"There are {len(num_item) - characters[0]['tot_num_weapons']} non-weapons")
# How many Items does each character have? (Return first 20 rows)
twenty_it = [len(chr['inv']) for chr in characters[:20]]
print(f"The first 20 people have {twenty_it} items")
# How many Weapons does each character have? (Return first 20 rows)
num_weap = [chr['weapons'] for chr in characters[:20]]
print(f"The first 20 people have {num_weap} weapons")
# On average, how many Items does each Character have?
avg_it = sum([len(chara['inv']) for chara in characters]) / len(characters)
print(f"Average number of items: {avg_it}")
# On average, how many Weapons does each character have?
avg_weap = sum([chara['weapons'] for chara in characters]) / len(characters)
print(f"Average number of weapons: {avg_weap}")


def conn_curs():
    dbn = "gdhyqmwk"
    user = "gdhyqmwk"

    with open("password.txt", 'r') as file:
        passw = file.read()

    host = "isilo.db.elephantsql.com"
    connec = psycopg2.connect(dbname=dbn, user=user,
                              password=passw, host=host)
    curss = connec.cursor()
    return curss, connec


curs, conn = conn_curs()
# How many passengers survived, and how many died?
curs.execute('SELECT count(name) FROM titanic')
people = curs.fetchall()[0][0]
curs.execute('SELECT count(name) FROM titanic WHERE survived = 1')
surv = curs.fetchall()[0][0]
print(f"{surv} people survived")
print(f"{people - surv} people died")
# How many passengers were in each class?
for i in range(1, 4):
    curs.execute(f'SELECT * FROM titanic WHERE pclass = {i}')
    temp = curs.fetchall()
    print(f"{len(temp)} people where class {i}")
# How many passengers survived/died within each class?
for i in range(1, 4):
    curs.execute(f'SELECT count(name) FROM titanic WHERE pclass = {i}')
    tot = curs.fetchall()[0][0]
    curs.execute(f'SELECT count(survived) FROM titanic WHERE pclass = {i} AND survived = 1')
    alive = curs.fetchall()[0][0]
    print(f"{alive} people survived from class {i}")
    print(f"{tot - alive} people died from class {i}")
# What was the average age of survivors vs nonsurvivors?
curs.execute('SELECT avg(age) FROM titanic WHERE survived = 1')
surv_age = curs.fetchall()[0][0]
curs.execute('SELECT avg(age) FROM titanic WHERE survived = 0')
dead_age = curs.fetchall()[0][0]
print(f"Avg age of survivor: {surv_age}")
print(f"Avg age of non-survivor {dead_age}")
# What was the average age of each passenger class?
for i in range(1, 4):
    curs.execute(f'SELECT avg(age) FROM titanic WHERE pclass = {i}')
    class_age = curs.fetchall()[0][0]
    print(f"Average age for class {i} ")
# What was the average fare by passenger class? By survival?
for i in range(1, 4):
    curs.execute(f'SELECT avg(age) FROM titanic WHERE pclass = {i} AND survived = 1')
    class_live_age = curs.fetchall()[0][0]
    print(f"Average age for class {i} that survived")
# How many siblings/spouses aboard on average, by passenger class? By survival?
"""THE REST OF THESE ARE NEEDLESSLY TEDIOUS SO I SKIPPED..."""
# How many parents/children aboard on average, by passenger class? By survival?
# Do any passengers have the same name?
# (Bonus! Hard, may require pulling and processing with Python)
# How many married couples were aboard the Titanic? Assume that two people (one Mr. and one Mrs.) with the same last name
# and with at least 1 sibling/spouse aboard are a married couple.

# connecting to postgresql
