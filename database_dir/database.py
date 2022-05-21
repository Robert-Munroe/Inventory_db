import sqlite3
from helper_functions import entrybuilder
from gui_dir import gui_windows


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
    general_id TEXT DEFAULT NULL,
    holding_location TEXT DEFAULT NULL,
    description TEXT DEFAULT NULL);''')


def create_table(cursor: sqlite3.Cursor):
    create_inventory_table(cursor)


def insert_into_inventory_table(cursor: sqlite3.Cursor, connection, entry_to_insert):
    cursor.executemany('''INSERT INTO founders_inventory(product_id, general_id, holding_location, description)
     VALUES(?,?,?,?)''', (entry_to_insert, ))
    connection.commit()


def get_product_id_from_db(cursor: sqlite3.Cursor, product_id):
    product_id = "'" + product_id + "'"
    result = cursor.execute(f'SELECT product_id FROM founders_inventory WHERE (product_id == {product_id});').fetchall()
    for row in result:
        result = row[0]
    product_id = product_id.replace("'", "")
    if result != product_id:
        return 0
    else:
        return 1


def get_product_info(cursor: sqlite3.Cursor, connection):
    product_info = []
    product_id = entrybuilder.ask_for_product_id_allow_duplicate()
    if product_id is None:
        return
    product_id = "'" + product_id + "'"
    result = cursor.execute(f'SELECT * FROM founders_inventory WHERE (product_id == {product_id});').fetchall()
    if not result:
        product_info = []
        return product_info

    for row in result:
        product_info.append(row[0])
        product_info.append(row[1])
        product_info.append(row[2])
        product_info.append(row[3])
    return product_info


def update_description(cursor: sqlite3.Cursor, connection):
    product_id = entrybuilder.ask_for_product_id_allow_duplicate()
    if product_id is None:
        gui_windows.pop_up_window("Error", "FSG ID")
        return
    product_id = "'" + product_id + "'"
    new_description = gui_windows.get_change_description()
    if new_description is None or new_description == "":
        gui_windows.pop_up_window("Error", "Description")
        return
    new_description = "'" + new_description + "'"
    cursor.execute(f'UPDATE founders_inventory SET description = {new_description} WHERE product_id = {product_id}')
    connection.commit()


def update_holding(cursor: sqlite3.Cursor, connection):
    product_id = entrybuilder.ask_for_product_id_allow_duplicate()
    if product_id is None:
        gui_windows.pop_up_window("Error", "FSG ID")
        return
    product_id = "'" + product_id + "'"
    new_holding_location = gui_windows.get_change_holding_location()
    if new_holding_location is None or new_holding_location == "":
        gui_windows.pop_up_window("Error", "Storage Location")
        return
    new_holding_location = "'" + new_holding_location + "'"
    cursor.execute(f'UPDATE founders_inventory SET holding_location = {new_holding_location}'
                   f'WHERE product_id = {product_id}')
    connection.commit()
