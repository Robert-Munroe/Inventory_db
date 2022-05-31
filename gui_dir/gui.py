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
        if event == "Update a Container Description":
            update_a_description_button()
        if event == "Update a Storage Location":
            update_a_holding_location_button()
        if event == "Exit" or event == simpleGui.WINDOW_CLOSED:
            break
    window.close()


def add_entry_button():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    product_id, general_id, holding_location, description, quantity, aggregate_form = gui_windows.get_entry_details()

    is_error = typechecking.is_product_id_formatted_correctly(product_id)

    if is_error == 1 or (general_id or holding_location or description or quantity or aggregate_form == "") \
            or aggregate_form != ('g' or 'ml' or 'container(s)' or 'bag(s)' or 'vial(s)'):
        error_list = []
        if is_error == 1:
            error_list.append(1)
        if general_id == "":
            error_list.append(2)
        if holding_location == "":
            error_list.append(3)
        if description == "":
            error_list.append(4)
        if quantity == "":
            error_list.append(5)
        if aggregate_form == "" or aggregate_form != ('g' or 'ml' or 'container(s)' or 'bag(s)' or 'vial(s)'):
            error_list.append(6)
        gui_windows.invalid_entry_window(error_list)
        return

    entry = [product_id, general_id, holding_location, description, quantity, aggregate_form]
    database.insert_into_inventory_table(db_cursor, connection, entry)


def view_a_sample_button():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    product_info = database.get_product_info(db_cursor, connection)
    gui_windows.view_a_sample_window(product_info)


def update_a_description_button():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    database.update_description(db_cursor, connection)


def update_a_holding_location_button():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    database.update_holding(db_cursor, connection)
