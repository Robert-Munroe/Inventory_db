import PySimpleGUI as simpleGui
from gui_dir import layouts, gui_windows
from database_dir import database
from helper_functions import typechecking


def main_window():
    layout = layouts.layout_main_window()

    window = simpleGui.Window("Founders Database", layout)

    while True:
        event, values = window.read()
        if event == "Add Entry":
            add_entry_button()
        if event == "View an FSG ID":
            view_a_sample_button()
        if event == "Update an FSG ID":
            update_an_fsg_id_button()
        if event == "Get logging information":
            get_logging_information_button()
        if event == "Update a Container Description":
            update_a_description_button()
        if event == "Update a Storage Location":
            update_a_holding_location_button()
        if event == "Update a sample's quantity":
            update_a_samples_quantity()
        if event == "Exit" or event == simpleGui.WINDOW_CLOSED:
            break
    window.close()


def add_entry_button():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)

    product_id, general_id, holding_location, description, quantity, aggregate_form, fsg_id_event_log\
        = gui_windows.get_entry_details()
    error_list = typechecking.is_entry_correct(product_id, general_id, holding_location, description,
                                               quantity, aggregate_form, fsg_id_event_log)

    if error_list:
        gui_windows.invalid_entry_window(error_list)
        return

    entry = [product_id, general_id, holding_location, description, quantity, aggregate_form, fsg_id_event_log]
    database.insert_into_inventory_table(db_cursor, connection, entry)


def view_a_sample_button():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    product_info = database.get_product_info(db_cursor, connection)
    gui_windows.view_a_sample_window(product_info)


def update_an_fsg_id_button():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)


def update_a_description_button():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    database.update_description(db_cursor, connection)


def update_a_holding_location_button():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    database.update_holding(db_cursor, connection)


def update_a_samples_quantity():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    database.update_quantity(db_cursor, connection)


def get_logging_information_button():
    return


def get_all_locations_button():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    product_id = gui_windows.get_product_id()
    if not product_id:
        return
    list_of_fsg_ids_and_locations = database.get_locations_of_product_id(product_id, db_cursor)
    if not list_of_fsg_ids_and_locations:
        gui_windows.pop_up_window('error', 'product_id')
    list_entries_lists = [list(i) for i in list_of_fsg_ids_and_locations]

    with open('list_of_product_location.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)


