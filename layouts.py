import PySimpleGUI as simpleGui


def layout_main_window():
    layout = [
        [simpleGui.Text("Welcome to the founders database")],
        [simpleGui.Button("Add Entry")],
        [simpleGui.Button("View an FSG ID")],
        [simpleGui.Button("Update a Container Description")],
        [simpleGui.Button("Update a Storage Location")],
        [simpleGui.Button("Exit")]
    ]
    return layout


def layout_entry_details():
    layout = [
        [simpleGui.Text("Please enter an FSG ID")],
        [simpleGui.Text("FSG ID: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("What is the product")],
        [simpleGui.Text("Product: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("Please enter a storage location")],
        [simpleGui.Text("Storage Location:", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("Please enter a describe the container")],
        [simpleGui.Text("Description:", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), simpleGui.Cancel()]
    ]
    return layout


def layout_get_fsg_id():
    layout = [
        [simpleGui.Text("Please enter an FSG ID")],
        [simpleGui.Text("FSG ID: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), simpleGui.Cancel()]
    ]
    return layout


def layout_change_description():
    layout = [
        [simpleGui.Text("Please enter a new container description")],
        [simpleGui.Text("Description: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), simpleGui.Cancel()]
    ]
    return layout


def layout_change_storage_location():
    layout = [
        [simpleGui.Text("Please enter a new storage location")],
        [simpleGui.Text("Location: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), simpleGui.Cancel()]
    ]
    return layout


def layout_pop_up_window(attribute):
    layout = [
        [simpleGui.Text(f"No valid {attribute} entered")]
    ]
    return layout


def layout_view_sample_info(fsg_id):
    layout = [
        [simpleGui.Text(f"FSG ID is: {fsg_id[0]}")],
        [simpleGui.Text(f"Product is: {fsg_id[1]}")],
        [simpleGui.Text(f"Storage Location is: {fsg_id[2]}")],
        [simpleGui.Text(f"Description of container is: {fsg_id[3]}")]
    ]
    return layout