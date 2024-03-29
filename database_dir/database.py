import sqlite3
import locations


def db_location():
    location = locations.set_personal_location()
    return location


def open_db(filename: str) -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def create_user_table(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_table(
    username TEXT PRIMARY KEY,
    user_password TEXT DEFAULT NULL,
    initials TEXT DEFAULT NULL,
    timestamp INT DEFAULT NULL,
    password_history TEXT DEFAULT NULL
    );''')


def create_inventory_table(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS founders_inventory(
    fsg_id TEXT PRIMARY KEY,
    storage_type TEXT DEFAULT NULL,
    product_id TEXT DEFAULT NULL,
    storage_position DEFAULT NULL,
    client_id TEXT DEFAULT NULL,
    storage_location TEXT DEFAULT NULL,
    addition_location_one TEXT DEFAULT NULL,
    addition_location_two TEXT DEFAULT NULL,
    container_description TEXT DEFAULT NULL,
    quantity INT DEFAULT NULL,
    aggregate_form TEXT DEFAULT NULL,
    fsg_id_event_log TEXT DEFAULT NULL
    );''')


def create_table(cursor: sqlite3.Cursor):
    create_inventory_table(cursor)
    create_user_table(cursor)


def insert_into_inventory_table(cursor: sqlite3.Cursor, connection, entry_to_insert):
    cursor.executemany('''INSERT INTO founders_inventory(fsg_id, storage_type, product_id, storage_position, client_id,
     storage_location, addition_location_one, addition_location_two, container_description, quantity, aggregate_form, 
     fsg_id_event_log) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (entry_to_insert,))
    connection.commit()


def get_log_in_from_db(cursor: sqlite3.Cursor, username, password):
    username = "'" + username + "'"
    result = cursor.execute(f'SELECT username FROM user_table WHERE (username == {username});').fetchall()
    for row in result:
        result = row[0]
    username = username.replace("'", "")
    if result != username:
        username = username.replace("'", "")
        return False, username, False
    username = "'" + username + "'"
    result = cursor.execute(f'SELECT user_password FROM user_table WHERE (username == {username});').fetchall()
    for row in result:
        result = row[0]
    if password != result:
        username = username.replace("'", "")
        return False, username, False
    result = cursor.execute(f'SELECT timestamp FROM user_table WHERE (username == {username});').fetchall()
    for row in result:
        result = row[0]
    timestamp = result
    username = username.replace("'", "")
    return True, username, timestamp


def does_fsg_id_exist(cursor: sqlite3.Cursor, fsg_id):
    fsg_id = "'" + fsg_id + "'"
    result = cursor.execute(f'SELECT fsg_id FROM founders_inventory WHERE (fsg_id == {fsg_id});').fetchall()
    for row in result:
        result = row[0]
    fsg_id = fsg_id.replace("'", "")
    if result == fsg_id:
        return True
    return False


def update_entry(cursor: sqlite3.Cursor, connection, fsg_id, storage_location, addition_location_one,
                 addition_location_two, storage_type, description, quantity, reason_for_change):
    fsg_id = "'" + fsg_id + "'"
    storage_location = "'" + storage_location + "'"
    storage_type = "'" + storage_type + "'"
    description = "'" + description + "'"
    quantity = "'" + quantity + "'"
    addition_location_one = "'" + addition_location_one + "'"
    addition_location_two = "'" + addition_location_two + "'"
    reason_for_change = append_event_log(cursor, fsg_id, reason_for_change)

    cursor.execute(f'UPDATE founders_inventory SET storage_location = {storage_location} WHERE fsg_id = {fsg_id}')
    cursor.execute(f'UPDATE founders_inventory SET addition_location_one = {addition_location_one} '
                   f'WHERE fsg_id = {fsg_id}')
    cursor.execute(f'UPDATE founders_inventory SET addition_location_two = {addition_location_two} '
                   f'WHERE fsg_id = {fsg_id}')
    cursor.execute(f'UPDATE founders_inventory SET storage_type = {storage_type} WHERE fsg_id = {fsg_id}')
    cursor.execute(f'UPDATE founders_inventory SET container_description = {description} WHERE fsg_id = {fsg_id}')
    cursor.execute(f'UPDATE founders_inventory SET quantity = {quantity} WHERE fsg_id = {fsg_id}')
    cursor.execute(f'UPDATE founders_inventory SET fsg_id_event_log = {reason_for_change} WHERE fsg_id = {fsg_id}')
    connection.commit()


def append_event_log(cursor: sqlite3.Cursor, fsg_id, reason_for_change):
    result = cursor.execute(f'SELECT fsg_id_event_log FROM founders_inventory WHERE (fsg_id == {fsg_id});').fetchall()
    for row in result:
        result = row[0]
    return "'" + result + reason_for_change + "'"


def get_product_info(cursor: sqlite3.Cursor, fsg_id):
    product_info = []
    if fsg_id is None:
        return
    fsg_id = "'" + fsg_id + "'"
    result = cursor.execute(f'SELECT * FROM founders_inventory WHERE (fsg_id == {fsg_id});').fetchall()
    if not result:
        product_info = []
        return product_info

    for row in result:
        product_info.append(row[0])
        product_info.append(row[2])
        product_info.append(row[3])
        product_info.append(row[5])
        product_info.append(row[6])
        product_info.append(row[7])
        product_info.append(row[8])
        product_info.append(row[9])
        product_info.append(row[10])
    return product_info


def get_previous_entry_info(fsg_id, cursor):
    fsg_id = "'" + fsg_id + "'"
    result = cursor.execute(f'SELECT storage_location, addition_location_one, addition_location_two,'
                            f' storage_type, container_description, quantity, aggregate_form  '
                            f'FROM founders_inventory WHERE (fsg_id == {fsg_id});')
    for row in result:
        previous_storage_location = row[0]
        previous_storage_location_one = row[1]
        previous_storage_location_two = row[2]
        previous_storage_type = row[3]
        previous_description = row[4]
        previous_quantity = row[5]
        previous_form = row[6]
        return previous_storage_location, previous_storage_location_one, previous_storage_location_two, \
            previous_storage_type, previous_description, previous_quantity, previous_form


def get_last_fsg_id_from_table(cursor):
    highest_fsg_id = ""
    entry = cursor.execute('SELECT * FROM founders_inventory ORDER BY fsg_id DESC LIMIT 1;')
    for row in entry:
        highest_fsg_id = row[0]

    return highest_fsg_id
