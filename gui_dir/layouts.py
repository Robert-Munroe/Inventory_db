import PySimpleGUI as simpleGui

import database_dir.database
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
    storage_location_menu_with_na = storage_locations.set_acceptable_locations_with_na()
    location_of_db = database_dir.database.db_location()
    connection, db_cursor = database_dir.database.open_db(location_of_db)
    last_fsg_id = database_dir.database.get_last_fsg_id_from_table(db_cursor)
    layout = [
        [simpleGui.Text("Please enter an FSG ID"), simpleGui.Push(),
         simpleGui.Text("Is this sample a retain or stability")],
        [simpleGui.Text("FSG ID: ", size=(20, 1)), simpleGui.InputText(f'{last_fsg_id}', size=(15, 1)),
         simpleGui.Combo(['Retain', 'Stability', 'Analytical'], default_value='Storage Type', size=(15, 1))],
        [simpleGui.Text("What is the product")],
        [simpleGui.Text("Product: ", size=(20, 1)), simpleGui.InputText(size=(15, 1))],
        [simpleGui.Text("Who is the client")],
        [simpleGui.Text("Client: ", size=(20, 1)), simpleGui.InputText(size=(15, 1))],
        [simpleGui.Text("Please enter a storage location")],
        [simpleGui.Text("Storage Location:", size=(20, 1)),
         simpleGui.Combo(storage_location_menu, default_value='Location', size=(15, 1))],
        [simpleGui.Text("Additional Storage:", size=(20, 1)),
         simpleGui.Combo(storage_location_menu_with_na, default_value='N/A', size=(15, 1)),
         simpleGui.Combo(storage_location_menu_with_na, default_value='N/A', size=(15, 1))],
        [simpleGui.Text("Please enter a describe the container")],
        [simpleGui.Text("Description:", size=(20, 1)), simpleGui.InputText(size=(15, 1))],
        [simpleGui.Text("Please enter the product's quantity and unit")],
        [simpleGui.Text("Quantity: X Unit: Y: ", size=(20, 1)), simpleGui.InputText(size=(15, 1)),
         simpleGui.Combo(['g', 'ml', 'container(s)', 'bag(s)', 'vial(s)'], default_value='Unit', size=(15, 1))],
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
        [simpleGui.Text(f"Storage Location is: {fsg_id[2]}")],
        [simpleGui.Text(f"Alternative storage locations are: {fsg_id[3]}, {fsg_id[4]}")],
        [simpleGui.Text(f"Description of container is: {fsg_id[5]}")],
        [simpleGui.Text(f"{fsg_id[6]} {fsg_id[7]}")]
    ]
    return layout


def layout_get_product_id():
    layout = [
        [simpleGui.Text("Please enter the product ID")],
        [simpleGui.Text("Product ID: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), simpleGui.Cancel()]
    ]
    return layout


def layout_get_entry_update(fsg_id, storage_location, addition_location_one, addition_location_two, storage_type,
                            description, quantity):
    storage_location_menu = storage_locations.set_acceptable_locations()
    storage_location_menu_with_na = storage_locations.set_acceptable_locations_with_na()
    layout = [
        [simpleGui.Text(f"You are making changes to {fsg_id}")],
        [simpleGui.Text("Please enter the storage location",), simpleGui.Push(),
         simpleGui.Text("Storage Type", size=(15, 1))],
        [simpleGui.Text("Storage Location:", size=(20, 1)),
         simpleGui.Combo(storage_location_menu, default_value=f'{storage_location}', size=(15, 1)), simpleGui.Push(),
         simpleGui.Combo(['Retain', 'Stability', 'Analytical'], default_value=f'{storage_type}', size=(15, 1))],
        [simpleGui.Text("Additional Storage", size=(20, 1)),
         simpleGui.Combo(storage_location_menu_with_na, default_value=f'{addition_location_one}', size=(15, 1)),
         simpleGui.Push(),
         simpleGui.Combo(storage_location_menu_with_na, default_value=f'{addition_location_two}', size=(15, 1))],
        [simpleGui.Text("Please enter the description")],
        [simpleGui.Text("Description: ", size=(20, 1)), simpleGui.InputText(f"{description}", size=(15, 1))],
        [simpleGui.Text("Please enter the product's quantity")],
        [simpleGui.Text("Quantity: ", size=(20, 1)), simpleGui.InputText(f"{quantity}", size=(15, 1))],
        [simpleGui.Text("Please enter a reason for your edit")],
        [simpleGui.Text("Edit Reason: ", size=(20, 1)), simpleGui.InputText(size=(15, 1))],
        [simpleGui.Submit(), simpleGui.Cancel()]
    ]
    return layout


def layout_logging_main_window():
    layout = [
        [simpleGui.Text("Welcome to logging")],
        [simpleGui.Button("FSG_ID by Product Name", size=(27, 1)), simpleGui.Push(),
         simpleGui.Button("Historic FSG_ID by Product Name", size=(27, 1))],
        [simpleGui.Button("FSG_ID in Storage Location", size=(27, 1)), simpleGui.Push(),
         simpleGui.Button("Historic FSG_ID in Storage Location", size=(27, 1))],
        [simpleGui.Button("FSG_ID by client", size=(27, 1)), simpleGui.Push(),
         simpleGui.Button("Historic FSG_ID by client", size=(27, 1))],
        [simpleGui.Button("Get all entries", size=(27, 1)), simpleGui.Push(),
         simpleGui.Button("Get all entries historic", size=(27, 1))],
        [simpleGui.Push(), simpleGui.Button("History of FSG_ID"), simpleGui.Push()],
        [simpleGui.Push(), simpleGui.Button("Exit")]
    ]
    return layout


def layout_get_storage_location():
    storage_location_menu = storage_locations.set_acceptable_locations()
    layout = [
        [simpleGui.Text("Storage Location:", size=(15, 1)),
         simpleGui.Combo(storage_location_menu, default_value="Location")],
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
