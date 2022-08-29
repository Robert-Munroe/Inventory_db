import PySimpleGUI as simpleGui

from database_dir import storage_locations, database
from gui_dir import layouts, logging_gui_buttons, gui_windows
from helper_functions import typechecking


def logging_main_window():
    layout = layouts.layout_logging_main_window()

    window = simpleGui.Window("Founders Database Logging", layout)

    while True:
        event, values = window.read()
        if event == "FSG_ID by Product Name":
            fsg_id_by_product_name_button()
        if event == "Historic FSG_ID by Product Name":
            fsg_id_by_product_name_button_historic()
        if event == "FSG_ID in Storage Location":
            storage_location_dump()
        if event == "Historic FSG_ID in Storage Location":
            storage_location_dump_historic()
        if event == "FSG_ID by client":
            fsg_id_by_client_button()
        if event == "Historic FSG_ID by client":
            fsg_id_by_client_historic_button()
        if event == "History of FSG_ID":
            fsg_id_dump()
        if event == "Exit" or event == simpleGui.WINDOW_CLOSED:
            break
    window.close()


def fsg_id_by_product_name_button():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    product_id = gui_windows.get_product_id()
    if not product_id:
        gui_windows.pop_up_window("Error", "No product ID entered")
        return
    logging_gui_buttons.fsg_by_product_name(product_id, db_cursor)


def fsg_id_by_product_name_button_historic():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    product_id = gui_windows.get_product_id()
    if not product_id:
        gui_windows.pop_up_window("Error", "No product ID entered")
        return
    logging_gui_buttons.fsg_by_product_name_historic(product_id, db_cursor)


def storage_location_dump():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    storage_location = gui_windows.get_storage_location()
    acceptable_locations = storage_locations.set_acceptable_locations()
    if storage_location not in acceptable_locations:
        gui_windows.pop_up_window("Error", "Not a valid storage location")
        return

    logging_gui_buttons.get_fsg_id_from_storage_location(storage_location, db_cursor)


def storage_location_dump_historic():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    acceptable_locations = storage_locations.set_acceptable_locations()
    storage_location = gui_windows.get_storage_location()

    if storage_location not in acceptable_locations:
        gui_windows.pop_up_window("Error", "Not a valid storage location")
        return

    logging_gui_buttons.get_fsg_id_from_storage_location_historic(storage_location, db_cursor)


def fsg_id_by_client_button():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    client = gui_windows.get_client_id()
    if not client:
        gui_windows.pop_up_window("Error", "No valid client")
        return
    logging_gui_buttons.get_fsg_id_by_client(client, db_cursor)


def fsg_id_by_client_historic_button():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    client = gui_windows.get_client_id()
    if not client:
        gui_windows.pop_up_window("Error", "No valid client")
        return
    logging_gui_buttons.get_fsg_id_by_client_historic(client, db_cursor)


def fsg_id_dump():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    fsg_id = gui_windows.get_fsg_id()
    if not fsg_id:
        gui_windows.pop_up_window("Error", "No valid FSG_ID")
        return

    is_error = typechecking.is_product_id_formatted_correctly_allow_duplicate(fsg_id)
    fsg_id = fsg_id.replace("s", "S")
    fsg_id = fsg_id.replace("r", "R")

    if is_error == 1:
        gui_windows.pop_up_window("Error", "FSG ID formatted incorrectly")
        return
    logging_gui_buttons.fsg_id_dump_button(fsg_id, db_cursor)
