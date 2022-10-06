import PySimpleGUI as simpleGui

from database_dir import database, storage_locations
from gui_dir import layouts, gui_windows, logging_gui
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

    product_id, storage_type, general_id, storage_position, client_id, holding_location, addition_location_one, addition_location_two, \
        description, quantity, aggregate_form, fsg_id_event_log = gui_windows.get_entry_details(initials)
    error_list = typechecking.is_entry_correct(product_id, storage_type, general_id, storage_position, client_id,
                                               holding_location, addition_location_one, addition_location_two,
                                               description, quantity, aggregate_form)

    if error_list:
        gui_windows.invalid_entry_window(error_list)
        return

    entry = [product_id, storage_type, general_id, storage_position,client_id, holding_location, addition_location_one,
             addition_location_two, description, quantity, aggregate_form, fsg_id_event_log]
    database.insert_into_inventory_table(db_cursor, connection, entry)


def view_a_sample_button():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    fsg_id = gui_windows.get_fsg_id()
    fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(fsg_id)
    product_info = database.get_product_info(db_cursor, fsg_id)
    gui_windows.view_a_sample_window(product_info)


def update_an_fsg_id_button(initials):
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    acceptable_locations = storage_locations.set_acceptable_locations()
    acceptable_locations_with_na = storage_locations.set_acceptable_locations_with_na()
    acceptable_storage_types = ['RETAIN', 'STABILITY', 'ANALYTICAL']
    fsg_id = gui_windows.get_fsg_id()
    fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(fsg_id)

    if not fsg_id:
        gui_windows.pop_up_window("Error", "FSG_ID does not exist")
        return

    does_fsg_id_exist = database.does_fsg_id_exist(db_cursor, fsg_id)

    if not does_fsg_id_exist:
        gui_windows.pop_up_window("Error", "FSG_ID does not exist")
        return

    previous_storage_location, previous_storage_location_one, previous_storage_location_two, \
        previous_storage_type, previous_description, previous_quantity, previous_form = \
        database.get_previous_entry_info(fsg_id, db_cursor)

    storage_location, addition_location_one, addition_location_two, storage_type, description, quantity,\
        reason_for_change = \
        gui_windows.get_update_entry(fsg_id, previous_storage_location, previous_storage_location_one,
                                     previous_storage_location_two, previous_storage_type, previous_description,
                                     previous_quantity, previous_form, initials)

    test_quantity = quantity.lstrip('-').replace('.', '', 1).replace('e-', '', 1).replace('e', '', 1)
    if storage_location == "" or storage_type == "" or description == "" or quantity == "" or reason_for_change == "":
        gui_windows.pop_up_window("Error", "You cannot make changes to an entry with a blank field")
        return
    if storage_location not in acceptable_locations:
        gui_windows.pop_up_window("Error", "Storage location does not exist")
        return

    if addition_location_one not in acceptable_locations_with_na or \
            addition_location_two not in acceptable_locations_with_na:
        gui_windows.pop_up_window("Error", "Additional locations are not valid")
        return

    if storage_type not in acceptable_storage_types:
        gui_windows.pop_up_window("Error", "Storage type is invalid")
        return
    if not test_quantity.isdigit():
        gui_windows.pop_up_window("Error", "Quantity is not a number")
        return

    database.update_entry(db_cursor, connection, fsg_id, storage_location, addition_location_one, addition_location_two,
                          storage_type, description, quantity, reason_for_change)


def get_logging_information_button():
    logging_gui.logging_main_window()
