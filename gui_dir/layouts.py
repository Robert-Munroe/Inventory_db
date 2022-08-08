import PySimpleGUI as simpleGui


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
    layout = [
        [simpleGui.Text("Please enter an FSG ID")],
        [simpleGui.Text("FSG ID: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("What is the product")],
        [simpleGui.Text("Product: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("Who is the client")],
        [simpleGui.Text("Client: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("Please enter a storage location")],
        [simpleGui.Text("Storage Location:", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("Please enter a describe the container")],
        [simpleGui.Text("Description:", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("Please enter the product's quantity and unit")],
        [simpleGui.Text("Quantity: X Unit: Y: ", size=(15, 1)), simpleGui.InputText(),
         simpleGui.Combo(['g', 'ml', 'container(s)', 'bag(s)', 'vial(s)'], default_value='Unit')],
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
    layout = [
        [simpleGui.Text(f"You are making changes to {fsg_id}")],
        [simpleGui.Text(f"Please enter the storage location")],
        [simpleGui.Text("Storage Location: ", size=(15, 1)), simpleGui.InputText(f"{storage_location}")],
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
        [simpleGui.Button("FSG_ID by Product Name"), simpleGui.Button("Historic FSG_ID by Product Name")],
        [simpleGui.Button("FSG_ID in storage location"), simpleGui.Button("Historic FSG_ID in storage location")],
        [simpleGui.Button("History by FSG_ID")],
        [simpleGui.Button("Exit")]
    ]
    return layout


def layout_get_storage_location():
    layout = [
        [simpleGui.Text("Please enter a storage location")],
        [simpleGui.Text("Storage Location: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), simpleGui.Cancel()]
    ]
    return layout
