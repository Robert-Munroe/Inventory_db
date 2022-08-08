from database_dir import logging_functions, database, storage_locations
from gui_dir import gui_windows
from helper_functions import typechecking


def fsg_by_product_name():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    product_id = gui_windows.get_product_id()
    if not product_id:
        gui_windows.pop_up_window("Error", "No product ID entered")
        return
    list_of_fsg_ids_and_locations = logging_functions.get_locations_of_product_id(product_id, db_cursor)
    if not list_of_fsg_ids_and_locations:
        gui_windows.pop_up_window('error', 'product_id')
    list_entries_lists = [list(i) for i in list_of_fsg_ids_and_locations]

    with open('list_of_product_location.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)


def fsg_by_product_name_historic():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    product_id = gui_windows.get_product_id()
    if not product_id:
        gui_windows.pop_up_window("Error", "No product ID entered")
        return
    list_of_fsg_ids_and_locations = logging_functions.get_locations_of_product_id_historic(product_id, db_cursor)
    if not list_of_fsg_ids_and_locations:
        gui_windows.pop_up_window('error', 'product_id')
    list_entries_lists = [list(i) for i in list_of_fsg_ids_and_locations]

    with open('list_of_product_location_historic.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)


def get_fsg_id_from_storage_location():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    acceptable_locations = storage_locations.set_acceptable_locations()
    storage_location = gui_windows.get_storage_location()

    if storage_location not in acceptable_locations:
        gui_windows.pop_up_window("Error", "Not a valid storage location")
        return

    list_of_records = logging_functions.get_fsg_id_from_storage_location(storage_location, db_cursor)
    if not list_of_records:
        gui_windows.pop_up_window('error', 'empty storage location')
        return
    list_entries_lists = [list(i) for i in list_of_records]

    with open(f'list_of_samples_in_{storage_location}.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)


def get_fsg_id_from_storage_location_historic():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    acceptable_locations = storage_locations.set_acceptable_locations()
    storage_location = gui_windows.get_storage_location()

    if storage_location not in acceptable_locations:
        gui_windows.pop_up_window("Error", "Not a valid storage location")
        return

    list_of_records = logging_functions.get_fsg_id_from_storage_location_historic(storage_location, db_cursor)
    if not list_of_records:
        gui_windows.pop_up_window('error', 'empty storage location')
        return

    list_entries_lists = [list(i) for i in list_of_records]

    with open(f'list_of_samples_in_{storage_location}_historic.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)


def get_fsg_id_by_client():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    client = gui_windows.get_client_id()

    list_of_records = logging_functions.get_fsg_id_by_client(client, db_cursor)

    if not list_of_records:
        gui_windows.pop_up_window('error', 'client id has no records')
        return

    entries_lists = [list(i) for i in list_of_records]

    with open(f'list_of_samples_for_{client}.txt', 'w') as f:
        for item in entries_lists:
            f.write("%s\n" % item)


def get_fsg_id_by_client_historic():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    client = gui_windows.get_client_id()

    list_of_records = logging_functions.get_fsg_id_by_client_historic(client, db_cursor)

    if not list_of_records:
        gui_windows.pop_up_window('error', 'client id has no records')
        return

    entries_lists = [list(i) for i in list_of_records]

    with open(f'list_of_samples_for_{client}_historic.txt', 'w') as f:
        for item in entries_lists:
            f.write("%s\n" % item)


def fsg_id_dump_button():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    fsg_id = gui_windows.get_fsg_id()

    is_error = typechecking.is_product_id_formatted_correctly_allow_duplicate(fsg_id)
    fsg_id = fsg_id.replace("s", "S")
    fsg_id = fsg_id.replace("r", "R")

    if is_error == 1:
        gui_windows.pop_up_window("Error", "FSG ID formatted incorrectly")
        return

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
