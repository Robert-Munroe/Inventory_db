import PySimpleGUI as simpleGui
from database_dir import storage_locations


def layout_main_window():
    layout = [
        [simpleGui.Text("Welcome to the founders database")],
        [simpleGui.Button("Add Entry")],
        [simpleGui.Button("View an FSG ID")],
        [simpleGui.Button("Update an FSG ID")],
        [simpleGui.Button("Get logging information")],
        [simpleGui.Button("Exit")]
    ]
    return layout


def layout_entry_details():
    storage_location_menu = storage_locations.set_acceptable_locations()
    layout = [
        [simpleGui.Text("Please enter an FSG ID")],
        [simpleGui.Text("FSG ID: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("What is the product")],
        [simpleGui.Text("Product: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("Who is the client")],
        [simpleGui.Text("Client: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("Please enter a storage location")],
        [simpleGui.Text("Storage Location:", size=(15, 1)),
         simpleGui.Combo(storage_location_menu, default_value='Location')],
        [simpleGui.Text("Please enter a describe the container")],
        [simpleGui.Text("Description:", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("Please enter the product's quantity and unit")],
        [simpleGui.Text("Quantity: X Unit: Y: ", size=(15, 1)), simpleGui.InputText(),
         simpleGui.Combo(['g', 'ml', 'container(s)', 'bag(s)', 'vial(s)'], default_value='Unit', readonly=True)],
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


def layout_pop_up_window(attribute):
    layout = [
        [simpleGui.Text(f"{attribute}")]
    ]
    return layout


def layout_view_sample_info(fsg_id):
    layout = [
        [simpleGui.Text(f"FSG ID is: {fsg_id[0]}")],
        [simpleGui.Text(f"Product is: {fsg_id[1]}")],
        [simpleGui.Text(f"Storage Location is: {fsg_id[3]}")],
        [simpleGui.Text(f"Description of container is: {fsg_id[4]}")],
        [simpleGui.Text(f"{fsg_id[5]} {fsg_id[6]}")]
    ]
    return layout


def layout_get_product_id():
    layout = [
        [simpleGui.Text("Please enter the product ID")],
        [simpleGui.Text("Product ID: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), simpleGui.Cancel()]
    ]
    return layout


def layout_get_entry_update(fsg_id, storage_location, description, quantity):
    storage_location_menu = storage_locations.set_acceptable_locations()
    layout = [
        [simpleGui.Text(f"You are making changes to {fsg_id}")],
        [simpleGui.Text(f"Please enter the storage location")],
        [simpleGui.Text("Storage Location:", size=(15, 1)),
         simpleGui.Combo(storage_location_menu, default_value=f'{storage_location}')],
        [simpleGui.Text(f"Please enter the description")],
        [simpleGui.Text("Description: ", size=(15, 1)), simpleGui.InputText(f"{description}")],
        [simpleGui.Text(f"Please enter the product's quantity")],
        [simpleGui.Text("Quantity: ", size=(15, 1)), simpleGui.InputText(f"{quantity}")],
        [simpleGui.Text(f"Please enter a reason for your edit")],
        [simpleGui.Text("Edit Reason: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), simpleGui.Cancel()]
    ]
    return layout


def layout_logging_main_window():
    layout = [
        [simpleGui.Text("Welcome to logging")],
        [simpleGui.Button("FSG_ID by Product Name", size=(27, 1)),
         simpleGui.Button("Historic FSG_ID by Product Name", size=(27, 1))],
        [simpleGui.Button("FSG_ID in Storage Location", size=(27, 1)),
         simpleGui.Button("Historic FSG_ID in Storage Location", size=(27, 1))],
        [simpleGui.Button("FSG_ID by client", size=(27, 1)),
         simpleGui.Button("Historic FSG_ID by client", size=(27, 1))],
        [simpleGui.Push(), simpleGui.Button("History of FSG_ID"), simpleGui.Push()],
        [simpleGui.Push(), simpleGui.Button("Exit")]
    ]
    return layout


def layout_get_storage_location():
    layout = [
        [simpleGui.Text("Please enter a storage location")],
        [simpleGui.Text("Storage Location: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), simpleGui.Cancel()]
    ]
    return layout


def layout_get_client_id():
    layout = [
        [simpleGui.Text("Please enter a client_id")],
        [simpleGui.Text("Client: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), simpleGui.Cancel()]
    ]
    return layout
