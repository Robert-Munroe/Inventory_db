from database_dir import logging_functions, database
from gui_dir import gui_windows


def fsg_by_product_name(product_id):
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    list_of_fsg_ids_and_locations = logging_functions.get_locations_of_product_id(product_id, db_cursor)
    if not list_of_fsg_ids_and_locations:
        gui_windows.pop_up_window('error', 'product_id')
    list_entries_lists = [list(i) for i in list_of_fsg_ids_and_locations]

    with open('fsg_by_product_name.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)
    f.close()


def fsg_by_product_name_historic(product_id):
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    list_of_fsg_ids_and_locations = logging_functions.get_locations_of_product_id_historic(product_id, db_cursor)
    if not list_of_fsg_ids_and_locations:
        gui_windows.pop_up_window('error', 'product_id')
    list_entries_lists = [list(i) for i in list_of_fsg_ids_and_locations]

    with open('fsg_by_product_name_historic.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)
    f.close()


def get_fsg_id_from_storage_location(storage_location):
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    list_of_records = logging_functions.get_fsg_id_from_storage_location(storage_location, db_cursor)
    if not list_of_records:
        gui_windows.pop_up_window('error', 'empty storage location')
        return
    list_entries_lists = [list(i) for i in list_of_records]

    with open(f'list_of_samples_in_{storage_location}.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)
    f.close()


def get_fsg_id_from_storage_location_historic(storage_location):
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    list_of_records = logging_functions.get_fsg_id_from_storage_location_historic(storage_location, db_cursor)
    if not list_of_records:
        gui_windows.pop_up_window('error', 'empty storage location')
        return

    list_entries_lists = [list(i) for i in list_of_records]

    with open(f'list_of_samples_in_{storage_location}_historic.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)
    f.close()


def get_fsg_id_by_client(client):
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    list_of_records = logging_functions.get_fsg_id_by_client(client, db_cursor)

    if not list_of_records:
        gui_windows.pop_up_window('error', 'client id has no records')
        return

    entries_lists = [list(i) for i in list_of_records]

    with open(f'list_of_samples_for_{client}.txt', 'w') as f:
        for item in entries_lists:
            f.write("%s\n" % item)
    f.close()


def get_fsg_id_by_client_historic(client):
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)

    list_of_records = logging_functions.get_fsg_id_by_client_historic(client, db_cursor)

    if not list_of_records:
        gui_windows.pop_up_window('error', 'client id has no records')
        return

    entries_lists = [list(i) for i in list_of_records]

    with open(f'list_of_samples_for_{client}_historic.txt', 'w') as f:
        for item in entries_lists:
            f.write("%s\n" % item)
    f.close()


def fsg_id_dump_button(fsg_id):
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)

    record = logging_functions.get_audit_log_by_fsg_id(fsg_id, db_cursor)

    if not record:
        gui_windows.pop_up_window('Error', 'no FSG ID found')
        return

    list_record = [list(i) for i in record]

    with open(f'audit_log_of_{fsg_id}.txt', 'w') as f:
        for item in list_record:
            f.write("%s\n" % item)

    with open(f'audit_log_of_{fsg_id}.txt', 'r') as f:
        for line in f.readlines():
            line = line.replace(',', ',\n').replace('[', "").replace(']', "").replace("'", "")
        with open(f'audit_log_of_{fsg_id}.txt', 'w') as new_file:
            new_file.write(line)
    f.close()
