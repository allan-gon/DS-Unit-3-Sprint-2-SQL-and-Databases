import pymongo
import sqlite3
import psycopg2


"""DONT WORRY, I RESET THE PASSWORD ON MY END"""
# connect to mongo db
passw = "OmnfnZvAb4Sm6Qfb"
dbname = 'rpg'
connection = ("mongodb+srv://diz8nBMbcD1RjaYE:" + passw +
              "@mod3.gn8np.mongodb.net/" + dbname +
              "?retryWrites=true&w=majority")
client = pymongo.MongoClient(connection)
db = client.test


# connect to local database
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# get character data
get_char = "SELECT * FROM charactercreator_character"
curs.execute(get_char)
characters = curs.fetchall()

# getting inventory from local db
get_inv = "SELECT character_id, item_id FROM charactercreator_character_inventory"
curs.execute(get_inv)
inv = curs.fetchall()

# what this does is pull out the inventory of a character so i can put in doc
# might need tweeking
inven = []
for i in range(1, 303):
    temp = []
    for tup in inv:
        if tup[0] == i:
            temp.append(tup[-1])
    inven.append(temp)

# get subclasses from local db
get_cler = "SELECT character_ptr_id FROM charactercreator_cleric"
curs.execute(get_cler)
cler = curs.fetchall()
is_cleric = [i[0] for i in cler]  # so if id in is_cleric subclass: cleric

get_fighter = "SELECT character_ptr_id FROM charactercreator_fighter"
curs.execute(get_fighter)
fighter = curs.fetchall()
is_fighter = [i[0] for i in fighter]  # so if id in is_fighter subclass: fighter

get_mage = "SELECT character_ptr_id FROM charactercreator_mage"
curs.execute(get_mage)
mage = curs.fetchall()
is_mage = [i[0] for i in mage]  # so if id in is_mage subclass: mage

get_necro = "SELECT mage_ptr_id FROM charactercreator_necromancer"
curs.execute(get_necro)
necro = curs.fetchall()
is_necro = [i[0] for i in necro]  # so if id in is_necro subclass: necro

get_thief = "SELECT character_ptr_id FROM charactercreator_thief"
curs.execute(get_thief)
thief = curs.fetchall()
is_thief = [i[0] for i in thief]  # so if id in is_cleric subclass: cleric

# get list of weapons
get_weap = "SELECT item_ptr_id FROM armory_weapon"
curs.execute(get_weap)
weap = curs.fetchall()
is_weapon = [i[0] for i in weap]

# deleting so you can run it
db.rpg.remove()

# insert dta into mongo db
for character in characters:
    name = character[1].replace('.', '')
    doc = {
        'id': character[0],
        'name': name,
        'lvl': character[2],
        'exp': character[3],
        'hp': character[4],
        'str': character[5],
        'int': character[6],
        'dex': character[7],
        'wisdom': character[8],
        'weapons': 0,
        'tot_num_weapons': 37
    }
    doc['inv'] = inven[doc['id'] - 1]
    for item in doc['inv']:
        if item in is_weapon:
            doc['weapons'] += 1
    if doc['id'] in is_necro:
        doc['subclass'] = 'necromancer'
    elif doc['id'] in is_mage:
        doc['subclass'] = 'mage'
    elif doc['id'] in is_thief:
        doc['subclass'] = 'thief'
    elif doc['id'] in is_cleric:
        doc['subclass'] = 'cleric'
    else:
        doc['subclass'] = 'fighter'

    db.rpg.insert_one(doc)

# # proof that it's there
print(list(db.rpg.find()))

# Q - How was working with MongoDB different from working with PostgreSQL?
# A - Different to access, simpler i think. Can't just see my tables
# What was easier, and what was harder?
# A - They were about the same but sql was probably simper because i can actually see
# my tables
