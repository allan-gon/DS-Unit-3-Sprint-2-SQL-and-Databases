import sqlite3


def create_table(connection):
    curs = connection.cursor()
    create_statement = """
    CREATE TABLE students(
      id INTEGER PRIMARY KEY AUTOINCREMENT.
      name CHAR(15) NOT NULL,
      num1 INTEGER,
      num2 INTEGER
    )
    """
    curs.execute(create_statement)
    curs.close()
    connection.commit()
    return


def insert_data(connection):
    curs = connection.cursor()
    my_data = [
        ('malven', 7, 10),
        ('steven', -3, 12),
        ('dondre', 80, -1)
    ]
    for datum in my_data:
        insert_statement = f"""
        INSERT into students
        (name, num1, num2)
        VALUES {datum}
        """
        curs.execute(insert_statement)
    curs.close()
    curs.commit()
    return


if __name__ == "__main__":
    conn = sqlite3.connect('example_db.sqlite3')
    create_table(conn)
    insert_data(conn)


# from functools import reduce  # map is built-in
# my_list = [1, 2, 3, 4]
# # Traditional (non-mapreduce) approach
# ssv_trad = sum([i**2 for i in my_list])  # That works fine - but what if we had 40 billion numbers?
# # We could use a mapreduce approach
# squared_values = map(lambda i: i**2, my_list)
#
#
# def add_numbers(x1, x2):
#     return x1 + x2
#
#
# ssv_mapreduce = reduce(add_numbers, squared_values)
# print('Sum of squared values (trad): ' + str(ssv_trad))
# print('Sum of squared values (map-reduce): ' + str(ssv_mapreduce))
