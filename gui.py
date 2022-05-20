import PySimpleGUI
import PySimpleGUI as simpleGui
import database
import gui_windows
import typechecking


def get_fsg_id():
    layout = [
        [simpleGui.Text("Please enter an FSG ID")],
        [simpleGui.Text("FSG ID: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), PySimpleGUI.Cancel()]
    ]
    window = simpleGui.Window("Enter FSG ID", layout)
    while True:
        event, values = window.read()
        if event == "Cancel":
            window.close()
            return
        if event == "Submit":
            product_id = values[0]
            window.close()
            return product_id
        window.close()
        return


def get_change_description():
    layout = [
        [simpleGui.Text("Please enter a new container description")],
        [simpleGui.Text("Description: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), PySimpleGUI.Cancel()]
    ]
    while True:
        window = simpleGui.Window("Change Description", layout)
        event, values = window.read()
        if event == "Cancel":
            description = 'error'
            window.Close()
            return description
        if event == "Submit":
            description = values[0]
            window.Close()
            return description
        window.close()
        description = 'error'
        return description


def get_change_holding_location():
    layout = [
        [simpleGui.Text("Please enter a new storage location")],
        [simpleGui.Text("Location: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), PySimpleGUI.Cancel()]
    ]
    while True:
        window = simpleGui.Window("Change Holding Location", layout)
        event, values = window.read()
        if event == "Cancel":
            holding_location = 'error'
            window.Close()
            return holding_location
        if event == "Submit":
            holding_location = values[0]
            window.Close()
            return holding_location
        window.close()
        holding_location = 'error'
        return holding_location


def get_product_info():
    layout = [
        [simpleGui.Text("Please enter the FSG ID you'd like to see")],
        [simpleGui.Text("FSG ID: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), PySimpleGUI.Cancel()]
    ]
    while True:
        window = simpleGui.Window("FSG ID Search", layout)
        event, values = window.read()
        if event == "Cancel":
            window.close()
            break
        if event == "Submit":
            product_id = values[0]
            runner = typechecking.is_product_id_formatted_correctly_allow_duplicate(product_id)
            if runner == 1:
                window.close()
                return
            window.close()
            return product_id
        window.close()
        break


def add_entry_button():
    connection, db_cursor = database.open_db("foundersinventorydb.sqlite")
    product_id, general_id, holding_location, description = gui_windows.get_entry_details()

    is_error = typechecking.is_product_id_formatted_correctly(product_id)

    if is_error == 1 or general_id == "" or holding_location == "" or description == "":
        error_list = []
        if is_error == 1:
            error_list.append(1)
        if general_id == "":
            error_list.append(2)
        if holding_location == "":
            error_list.append(3)
        if description == "":
            error_list.append(4)
        gui_windows.invalid_entry_window(error_list)
        return

    entry = [product_id, general_id, holding_location, description]
    database.insert_into_inventory_table(db_cursor, connection, entry)


def view_a_sample_button():
    connection, db_cursor = database.open_db("foundersinventorydb.sqlite")
    product_info = database.get_product_info(db_cursor, connection)

    if not product_info:
        layout_for_bad_entry = [
            [simpleGui.Text("Error, entry does not exist")]
        ]
        view_a_sample_window = simpleGui.Window("Warning", layout_for_bad_entry)

    if product_info:
        layout_for_valid_entry = [
            [simpleGui.Text(f"FSG ID is: {product_info[0]}")],
            [simpleGui.Text(f"Product is: {product_info[1]}")],
            [simpleGui.Text(f"Storage Location is: {product_info[2]}")],
            [simpleGui.Text(f"Description of container is: {product_info[3]}")]
        ]
        view_a_sample_window = simpleGui.Window(f"Entry of {product_info[0]}", layout_for_valid_entry)

    while True:
        event, values = view_a_sample_window.read()
        if event == simpleGui.WINDOW_CLOSED:
            break


def update_a_description_button():
    connection, db_cursor = database.open_db("foundersinventorydb.sqlite")
    database.update_description(db_cursor, connection)


def update_a_holding_location_button():
    connection, db_cursor = database.open_db("foundersinventorydb.sqlite")
    database.update_holding(db_cursor, connection)
