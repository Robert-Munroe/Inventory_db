import PySimpleGUI as simpleGui
import layouts


def pop_up_window(window_type, attribute):
    layout = layouts.layout_pop_up_window(attribute)
    window = simpleGui.Window(window_type, layout)
    while_pop_up_window_is_true_loop(window)


def while_pop_up_window_is_true_loop(window):
    while True:
        event, values = window.read()
        if event == simpleGui.WINDOW_CLOSED:
            break


def get_entry_details():
    layout = layouts.layout_entry_details()
    window = simpleGui.Window("Add an Entry", layout)
    while True:
        event, values = window.read()
        if event == "Cancel":
            window.close()
            product_id = "error"
            general_id = ""
            holding_location = ""
            description = ""
            return product_id, general_id, holding_location, description
        if event == "Submit":
            product_id = values[0]
            general_id = values[1]
            holding_location = values[2]
            description = values[3]
            window.close()
            return product_id, general_id, holding_location, description
        product_id = "error"
        general_id = ""
        holding_location = ""
        description = ""
        window.close()
        return product_id, general_id, holding_location, description


def invalid_entry_window(error_list):
    error_text = ""
    for i in range(len(error_list)):
        if error_list[i] == 1:
            error_text = error_text + "FSG ID is invalid or blank "
        if error_list[i] == 2:
            error_text = error_text + "product field is blank "
        if error_list[i] == 3:
            error_text = error_text + "storage location is blank "
        if error_list[i] == 4:
            error_text = error_text + "container description is blank "

    layout = [
        [simpleGui.Text("The entry was invalid and has not been added to the database")],
        [simpleGui.Text(f"The {error_text}")]
    ]

    error_window = simpleGui.Window("Error", layout)
    while_pop_up_window_is_true_loop(error_window)


def get_fsg_id():
    layout = layouts.layout_get_fsg_id()
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


def view_a_sample_window(product_info):
    if not product_info:
        pop_up_window("Error", "Entry")
        return

    if product_info:
        layout_for_valid_entry = layouts.layout_view_sample_info(product_info)

        window = simpleGui.Window(f"Entry of {product_info[0]}", layout_for_valid_entry)
        while_pop_up_window_is_true_loop(window)


def get_change_description():
    layout = layouts.layout_change_description()
    while True:
        window = simpleGui.Window("Change Description", layout)
        event, values = window.read()
        if event == "Cancel":
            window.close()
            return
        if event == "Submit":
            description = values[0]
            window.Close()
            return description
        window.close()
        return


def get_change_holding_location():
    layout = layouts.layout_change_storage_location()
    while True:
        window = simpleGui.Window("Change Storage Location", layout)
        event, values = window.read()
        if event == "Cancel":
            window.Close()
            return
        if event == "Submit":
            holding_location = values[0]
            window.Close()
            return holding_location
        window.close()
        return
