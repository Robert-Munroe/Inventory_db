import PySimpleGUI as simpleGui
from gui_dir import layouts, gui_windows, logging_gui
from database_dir import database, storage_locations
from helper_functions import typechecking, entrybuilder


def main_window(initials):
    layout = layouts.layout_main_window()
    window = simpleGui.Window("Founders Database", layout)
    initials = initials

    while True:
        event, values = window.read()
        if event == "Add Entry":
            add_entry_button(initials)
        if event == "View an FSG ID":
            view_a_sample_button()
        if event == "Update an FSG ID":
            update_an_fsg_id_button(initials)
        if event == "Get logging information":
            get_logging_information_button()
        if event == "Exit" or event == simpleGui.WINDOW_CLOSED:
            break
    window.close()


def add_entry_button(initials):
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)

    product_id, general_id, holding_location, description, quantity, aggregate_form, fsg_id_event_log \
        = gui_windows.get_entry_details(initials)
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


def update_an_fsg_id_button(initials):
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    acceptable_locations = storage_locations.set_acceptable_locations()

    fsg_id = entrybuilder.ask_for_product_id_allow_duplicate()

    if not fsg_id:
        gui_windows.pop_up_window("Error", "FSG_ID does not exist")
        return

    does_fsg_id_exist = database.does_fsg_id_exist(db_cursor, fsg_id)

    if not does_fsg_id_exist:
        gui_windows.pop_up_window("Error", "FSG_ID does not exist")
        return

    storage_location, description, quantity, reason_for_change = gui_windows.get_update_entry(fsg_id, initials)
    test_quantity = quantity.lstrip('-').replace('.', '', 1).replace('e-', '', 1).replace('e', '', 1)

    if storage_location == "" or description == "" or quantity == "" or reason_for_change == "":
        gui_windows.pop_up_window("Error", "You cannot make changes to an entry with a blank field")
        return
    if storage_location not in acceptable_locations:
        gui_windows.pop_up_window("Error", "Storage Location does not exist")
        return
    if not test_quantity.isdigit():
        gui_windows.pop_up_window("Error", "Quantity is not a number")
        return

    database.update_entry(db_cursor, connection, fsg_id, storage_location, description, quantity, reason_for_change)


def get_logging_information_button():
    logging_gui.logging_main_window()


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
