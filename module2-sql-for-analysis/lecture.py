import psycopg2
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


if __name__ == "__main__":
    pg_curs, pg_conn = conn_curs()

    create_table = """
    CREATE TABLE test_table (
      id SERIAL PRIMARY KEY,
      name varchar(40) NOT NULL,
      data JSONB
    );
    """
    pg_curs.execute(create_table)
    pg_conn.commit()

    pg_curs.execute('SELECT * FROM test_table;')
    data = pg_curs.fetchall()

    print(data)

    insert_statement = """
    INSERT INTO test_table (name, data) VALUES
    (
        'Zaphod Beeblebrox',
        '{"key": "value", "key2": true}'::JSONB
    )
    """

    pg_curs.execute(insert_statement)
    pg_conn.commit()

    # ETL
    # Extract - get data
    # Transform - weak as appropriate
    # Load - insert into destination

    s_conn = sqlite3.connect('rpg_db.sqlite3')
    s_curs = s_conn.cursor()

    get_char = "SELECT * FROM charactercreator_character"
    s_curs.execute(get_char)
    characters = s_curs.fetchall()

    # figure out type for schema
    s_curs.execute('PRAGMA table_info(charactercreator_character);')
    s_curs.fetchall()

    create_character_table = """
    CREATE TABLE charactercreator_character (
      character_id SERIAL PRIMARY KEY,
      name VARCHAR(30),
      level INT,
      exp INT,
      hp INT,
      strength INT,
      intelligence INT,
      dexterity INT,
      wisdom INT
    );
    """

    pg_curs.execute(create_character_table)
    pg_conn.commit()

    for character in characters:
        insert_character = """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES """ + str(character[1:]) + ";"
        pg_curs.execute(insert_character)

    pg_conn.commit()

    pg_curs.execute('SELECT * FROM charactercreator_character LIMIT 5;')
    pg_curs.fetchall()
