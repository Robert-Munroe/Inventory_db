from database_dir import database
from gui_dir import gui_windows
from helper_functions import typechecking


def fsg_by_product_name():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    product_id = gui_windows.get_product_id()
    if not product_id:
        gui_windows.pop_up_window("Error", "No product ID entered")
        return
    list_of_fsg_ids_and_locations = database.get_locations_of_product_id(product_id, db_cursor)
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
    list_of_fsg_ids_and_locations = database.get_locations_of_product_id_historic(product_id, db_cursor)
    if not list_of_fsg_ids_and_locations:
        gui_windows.pop_up_window('error', 'product_id')
    list_entries_lists = [list(i) for i in list_of_fsg_ids_and_locations]

    with open('list_of_product_location_historic.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)