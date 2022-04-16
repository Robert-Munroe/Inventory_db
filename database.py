import sqlite3
import typechecking


def open_db(filename: str) -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def create_inventory_table(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS founders_inventory(
    product_id TEXT PRIMARY KEY,
    client_id TEXT DEFAULT NULL,
    general_id TEXT DEFAULT NULL,
    number_of_containers INT DEFAULT 0,
    current_number_of_containers INT DEFAULT 0,
    date_received TEXT DEFAULT NULL,
    holding_location TEXT DEFAULT NULL,
    in_out TEXT DEFAULT NULL,
    description TEXT DEFAULT NULL);''')


def create_table(cursor: sqlite3.Cursor):
    create_inventory_table(cursor)


def insert_into_inventory_table(cursor: sqlite3.Cursor, connection, entry_to_insert):
    cursor.executemany('''INSERT INTO founders_inventory(product_id, client_id, general_id, number_of_containers,
     current_number_of_containers, date_received, holding_location, in_out, description)
     VALUES(?,?,?,?,?,?,?,?,?)''', (entry_to_insert, ))
    connection.commit()


def get_product_info(cursor: sqlite3.Cursor, connection):
    product_id = input("Please enter the product ID you'd like to view")
    is_error = typechecking.is_product_id_formatted_correctly(product_id)
    while is_error == 1:
        product_id = input("Please enter product ID in this format [last two of year ##][S,R][ID CODE ####]")
        is_error = typechecking.is_product_id_formatted_correctly(product_id)
    product_id = "'" + product_id + "'"
    result = cursor.execute(f'SELECT * FROM founders_inventory WHERE (product_id == {product_id});').fetchall()
    for row in result:
        print(f'Product ID: {row[0]}\nClient ID: {row[1]}\nGeneral ID: {row[2]}\n'
              f'Number of containers when received: {row[3]}\nCurrent number of containers: {row[4]}\n'
              f'Date Received: {row[5]}\nHolding Location: {row[6]}\nIn/Out: {row[7]}\n'
              f'Description: {row[8]}\n\n\n')
