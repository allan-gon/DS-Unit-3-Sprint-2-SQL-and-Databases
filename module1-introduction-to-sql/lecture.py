import sqlite3

# connect to database
conn = sqlite3.connect('rpg_db.sqlite3')
# make a cursor
curs = conn.cursor()
# write query (string that's valid sql)
query = 'SELECT * FROM armory_item;'  # get everything from armory_item
# execute query
curs.execute(query)
# fetch results
results = curs.fetchall()

print(results[:5])

# curs = conn.cursor()
# create_statement = 'CREATE TABLE test(name char(20), age int);'
# curs.execute()
# curs.fetchall()

# insert_statement = "INSERT INTO test (name, age) Values ('John', 20);"
# curs.execute(insert_statement)
# curs.close()
# conn.commit()

# COUNT(*) is len of *
# COUNT(DISTINCT(*)) is nunique
# SELECT *comma separated* values FROM *database* LIMIT *condition or num*
# SELECT character_id, name
# FROM charactercreator_character
# WHERE character_id > 50 AND character_id < 55;
# Equivalent to
# WHERE character_id BETWEEN 51 AND 54;

# SELECT * FROM a
# INNER JOIN b
# ON cola = colb;

