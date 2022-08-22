# import sqlite3
from database_dir import database, log_in_database_functions
from gui_dir import logging_gui_buttons

# creating testing database
location_of_db = r"I:\database\founder_test_db.sqlite"
connection, db_cursor = database.open_db(location_of_db)
db_cursor.execute('DROP TABLE IF EXISTS founders_inventory;')
connection.commit()
db_cursor.execute('DROP TABLE IF EXISTS user_table;')
connection.commit()
database.create_table(db_cursor)
database.create_user_table(db_cursor)
database.create_inventory_table(db_cursor)

entry_for_inventory_table = ["21S0001", "WATER", "CLIENT-0003", "F7R1S1BA", "CLEAR JAR", 5, "G", "EVENT_LOG, "]
database.insert_into_inventory_table(db_cursor, connection, entry_for_inventory_table)
entry_for_inventory_table = ["21S0002", "WATER", "CLIENT-0003", "F7R1S1BA", "CLEAR JAR", 0, "G", "EVENT_LOG, "]
database.insert_into_inventory_table(db_cursor, connection, entry_for_inventory_table)

entry_for_user_table = ["FSGRAMUNROE", "Pa%%w0rd", "RAM", 22218]
log_in_database_functions.insert_into_user_table(db_cursor, connection, entry_for_user_table)


def test_log_in():
    logged_in, navigator, timestamp = database.get_log_in_from_db(db_cursor, "FSGRAMUNROE", "Pa%%w0rd")
    assert logged_in
    assert navigator == "FSGRAMUNROE"
    assert timestamp == 22218

    logged_in, navigator, timestamp = database.get_log_in_from_db(db_cursor, "FSGRAMUNROE", "")
    assert not logged_in
    assert navigator == "FSGRAMUNROE"
    assert not timestamp

    logged_in, navigator, timestamp = database.get_log_in_from_db(db_cursor, "", "")
    assert not logged_in
    assert navigator == ""
    assert not timestamp

    logged_in, navigator, timestamp = database.get_log_in_from_db(db_cursor, "not_in_table", "")
    assert not logged_in
    assert navigator == "not_in_table"
    assert not timestamp


def test_get_fsg_id():
    fsg_id = database.does_fsg_id_exist(db_cursor, "21S0001")
    assert fsg_id
    fsg_id = database.does_fsg_id_exist(db_cursor, "")
    assert not fsg_id
    fsg_id = database.does_fsg_id_exist(db_cursor, "26S0001")
    assert not fsg_id


def test_append_error_log():
    new_event_log = database.append_event_log(db_cursor, "'21S0001'", "this is a new new message")
    assert new_event_log == "'EVENT_LOG, this is a new new message'"


def test_get_product_details():
    product_info = database.get_product_info(db_cursor, "21S0001")
    assert product_info == ["21S0001", "WATER", "CLIENT-0003", "F7R1S1BA", "CLEAR JAR", 5, "G"]
    product_info = database.get_product_info(db_cursor, "")
    assert product_info == []
    product_info = database.get_product_info(db_cursor, "21S0008")
    assert product_info == []


def test_does_user_exit():
    does_user_exist = log_in_database_functions.user_exist(db_cursor, "FSGRAMUNROE")
    assert does_user_exist
    does_user_exist = log_in_database_functions.user_exist(db_cursor, "")
    assert not does_user_exist
    does_user_exist = log_in_database_functions.user_exist(db_cursor, "not there")
    assert not does_user_exist


def test_get_user_initials():
    initials = log_in_database_functions.get_user_initials(db_cursor, "FSGRAMUNROE")
    assert initials == "RAM"
    initials = log_in_database_functions.get_user_initials(db_cursor, "")
    assert not initials
    initials = log_in_database_functions.get_user_initials(db_cursor, "not in database")
    assert not initials


def test_get_all_users():
    result = log_in_database_functions.get_all_users(db_cursor)
    assert result == [("FSGRAMUNROE", "Pa%%w0rd", "RAM", 22218)]


def test_change_password():
    log_in_database_functions.change_user_password(db_cursor, connection, "FSGRAMUNROE", "Pa$$w0rd", 22219)
    result = log_in_database_functions.get_all_users(db_cursor)
    assert result == [("FSGRAMUNROE", "Pa$$w0rd", "RAM", 22219)]


def test_logging_product_id():
    logging_gui_buttons.fsg_by_product_name("WATER", db_cursor)
    f = open(r'C:\Users\rmunr\PycharmProjects\foundersinventorydatabase\tests\db_tests\fsg_by_product_name.txt', "r")
    expected_value = ["['21S0001', 'WATER', 'CLIENT-0003', 'F7R1S1BA', 'CLEAR JAR', 5, 'G', "
                      "'EVENT_LOG, ']\n"]
    readfile = f.readlines()
    f.close()
    assert readfile == expected_value


def test_logging_product_id_historic():
    logging_gui_buttons.fsg_by_product_name_historic("WATER", db_cursor)
    path = r'C:\Users\rmunr\PycharmProjects\foundersinventorydatabase\tests\db_tests\fsg_by_product_name_historic.txt'
    f = open(path, "r")
    expected_value = ["['21S0001', 'WATER', 'CLIENT-0003', 'F7R1S1BA', 'CLEAR JAR', 5, 'G', "
                      "'EVENT_LOG, ']\n",
                      "['21S0002', 'WATER', 'CLIENT-0003', 'F7R1S1BA', 'CLEAR JAR', 0, 'G', "
                      "'EVENT_LOG, ']\n"]
    readfile = f.readlines()
    f.close()
    assert readfile == expected_value
