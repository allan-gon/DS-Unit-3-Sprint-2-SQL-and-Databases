import sqlite3
import pandas as pd

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()


def fetch_index(query, cursor=curs):
    cursor.execute(query)
    return cursor.fetchall()[0][0]


num_chars = fetch_index("SELECT COUNT(character_id) FROM charactercreator_character")
num_mages = fetch_index("SELECT COUNT(character_ptr_id) FROM charactercreator_mage")
num_thieves = fetch_index("SELECT COUNT(character_ptr_id) FROM charactercreator_thief")
num_necro = fetch_index("SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer")
num_cleric = fetch_index("SELECT COUNT(character_ptr_id) FROM charactercreator_cleric")
num_fighter = fetch_index("SELECT COUNT(character_ptr_id) FROM charactercreator_fighter")

# Q - How many total Items?
query = "SELECT item_id FROM armory_item"
curs.execute(query)
num_items = len(curs.fetchall())

# Q - How many of the Items are weapons? How many are not?
query = "SELECT * FROM armory_weapon"
curs.execute(query)
num_weapons = len(curs.fetchall())

# Q - How many Items does each character have? (Return first 20 rows)
query = """
SELECT count(character_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;
"""
curs.execute(query)
x = curs.fetchall()
it_pr_chr = [i[0] for i in x]

# Q - How many Weapons does each character have? (Return first 20 rows)
query = """
SELECT count(character_id) FROM
(SELECT character_id, item_ptr_id
FROM charactercreator_character_inventory, armory_weapon
WHERE item_id = item_ptr_id
LIMIT 30)
GROUP BY character_id;
"""
# here limit is 30- so i can get first 20 characters, because at 30 observations 20 character id's are captured
# But at 20 observations only 14 characters are captured

curs.execute(query)
x = curs.fetchall()
wp_pr_chr = [i[0] for i in x]

avg_items = fetch_index(
    """
    SELECT avg(num_item) FROM
    (SELECT count(character_id) as num_item
    FROM charactercreator_character_inventory
    GROUP BY character_id);
    """
)

avg_weapons = fetch_index(
    """
    SELECT avg(num_weap) from
    (SELECT count(character_id) as num_weap
    FROM
    (SELECT character_id, item_ptr_id
    FROM charactercreator_character_inventory, armory_weapon
    WHERE item_id = item_ptr_id)
    GROUP BY character_id);
    """
)


if __name__ == "__main__":
    # Q1
    print(f"Total number of characters: {num_chars}")
    # Q2
    print(f"Number of mages: {num_mages}")
    print(f"Number of thieves: {num_thieves}")
    print(f"Number of necromancers: {num_necro}")
    print(f"Number of clerics: {num_cleric}")
    print(f"Number of fighter: {num_fighter}")
    # Q3
    print(f"Number of items: {num_items}")
    # Q4
    print(f"Number of weapons: {num_weapons}")
    print(f"Number of non-weapons: {num_items - num_weapons}")
    # Q5
    print(f'Items per character(only first 20): {it_pr_chr}')
    # Q6
    print(f'Weapons per character(only first 20): {wp_pr_chr}')
    # Q6
    print(f"Average number of items: {avg_items}")
    # Q7
    print(f"Average number of weapons: {avg_weapons}")


# [3, 3, 2, 4, 4, 1, 5, 3, 4, 4, 3, 3, 4, 4, 4, 1, 5, 5, 3, 1]
# [0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
