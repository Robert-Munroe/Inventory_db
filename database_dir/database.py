import sqlite3
from helper_functions import entrybuilder
from gui_dir import gui_windows


def db_location():
    location = r"D:\foundersinventorydb.sqlite"
    return location


def open_db(filename: str) -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def create_inventory_table(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS founders_inventory(
    fsg_id TEXT PRIMARY KEY,
    product_id TEXT DEFAULT NULL,
    storage_location TEXT DEFAULT NULL,
    container_description TEXT DEFAULT NULL,
    quantity INT DEFAULT NULL,
    aggregate_form TEXT DEFAULT NULL
    );''')


def create_table(cursor: sqlite3.Cursor):
    create_inventory_table(cursor)


def insert_into_inventory_table(cursor: sqlite3.Cursor, connection, entry_to_insert):
    cursor.executemany('''INSERT INTO founders_inventory(fsg_id, product_id, storage_location, container_description, 
    quantity, aggregate_form)
     VALUES(?, ?, ?, ?, ?, ?)''', (entry_to_insert, ))
    connection.commit()


def get_product_id_from_db(cursor: sqlite3.Cursor, fsg_id):
    fsg_id = "'" + fsg_id + "'"
    result = cursor.execute(f'SELECT fsg_id FROM founders_inventory WHERE (fsg_id == {fsg_id});').fetchall()
    for row in result:
        result = row[0]
    fsg_id = fsg_id.replace("'", "")
    if result != fsg_id:
        return 0
    else:
        return 1


def get_product_info(cursor: sqlite3.Cursor, connection):
    product_info = []
    fsg_id = entrybuilder.ask_for_product_id_allow_duplicate()
    if fsg_id is None:
        return
    fsg_id = "'" + fsg_id + "'"
    result = cursor.execute(f'SELECT * FROM founders_inventory WHERE (fsg_id == {fsg_id});').fetchall()
    if not result:
        product_info = []
        return product_info

    for row in result:
        product_info.append(row[0])
        product_info.append(row[1])
        product_info.append(row[2])
        product_info.append(row[3])
        product_info.append(row[4])
        product_info.append(row[5])
    return product_info


def update_description(cursor: sqlite3.Cursor, connection):
    fsg_id = entrybuilder.ask_for_product_id_allow_duplicate()
    if fsg_id is None:
        gui_windows.pop_up_window("Error", "FSG ID")
        return
    fsg_id = "'" + fsg_id + "'"
    result = cursor.execute(f'SELECT * FROM founders_inventory WHERE (fsg_id == {fsg_id});').fetchall()
    if not result:
        gui_windows.pop_up_window("Error", "FSG ID")
        return
    new_description = gui_windows.get_change_description()
    if new_description is None or new_description == "":
        gui_windows.pop_up_window("Error", "Description")
        return
    new_description = "'" + new_description + "'"
    cursor.execute(f'UPDATE founders_inventory SET container_description = {new_description} WHERE fsg_id = {fsg_id}')
    connection.commit()


def update_holding(cursor: sqlite3.Cursor, connection):
    fsg_id = entrybuilder.ask_for_product_id_allow_duplicate()
    if fsg_id is None:
        gui_windows.pop_up_window("Error", "FSG ID")
        return
    fsg_id = "'" + fsg_id + "'"
    result = cursor.execute(f'SELECT * FROM founders_inventory WHERE (fsg_id == {fsg_id});').fetchall()
    if not result:
        gui_windows.pop_up_window("Error", "FSG ID")
        return
    new_holding_location = gui_windows.get_change_holding_location()
    if new_holding_location is None or new_holding_location == "":
        gui_windows.pop_up_window("Error", "Storage Location")
        return
    new_holding_location = "'" + new_holding_location + "'"
    cursor.execute(f'UPDATE founders_inventory SET storage_location = {new_holding_location}'
                   f'WHERE fsg_id = {fsg_id}')
    connection.commit()


def update_quantity(cursor: sqlite3.Cursor, connection):
    fsg_id = entrybuilder.ask_for_product_id_allow_duplicate()
    if fsg_id is None:
        gui_windows.pop_up_window("Error", "FSG ID")
        return
    fsg_id = "'" + fsg_id + "'"
    result = cursor.execute(f'SELECT * FROM founders_inventory WHERE (fsg_id == {fsg_id});').fetchall()
    if not result:
        gui_windows.pop_up_window("Error", "FSG ID")
        return
    new_quantity = gui_windows.get_product_quantity()
    if new_quantity is None:
        gui_windows.pop_up_window("Error", "Quantity")
        return
    test_unit = new_quantity.lstrip('-').replace('.', '', 1).replace('e-', '', 1).replace('e', '', 1)
    if new_quantity is None or test_unit.isdigit() == False:
        gui_windows.pop_up_window("Error", "Quantity is invalid")
        return
    cursor.execute(f'UPDATE founders_inventory SET quantity = {new_quantity} WHERE fsg_id = {fsg_id}')
    connection.commit()
