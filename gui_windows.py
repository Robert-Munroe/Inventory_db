import PySimpleGUI as simpleGui
import PySimpleGUI


def get_entry_details():
    layout = [
        [simpleGui.Text("Please enter an FSG ID")],
        [simpleGui.Text("FSG ID: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("What is the product")],
        [simpleGui.Text("Product: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("Please enter a storage location")],
        [simpleGui.Text("Storage Location:", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("Please enter a describe the container")],
        [simpleGui.Text("Description:", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), PySimpleGUI.Cancel()]
    ]
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
    while True:
        event, values = error_window.read()
        if event == simpleGui.WINDOW_CLOSED:
            break


def get_layout_main_window():
    layout = [
        [simpleGui.Text("Welcome to the founders database")],
        [simpleGui.Button("Add Entry")],
        [simpleGui.Button("View an FSG ID")],
        [simpleGui.Button("Update a Container Description")],
        [simpleGui.Button("Update a Storage Location")],
        [simpleGui.Button("Exit")]
    ]
    return layout
