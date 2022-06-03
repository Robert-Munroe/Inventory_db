import PySimpleGUI as simpleGui


def layout_main_window():
    layout = [
        [simpleGui.Text("Welcome to the founders database")],
        [simpleGui.Button("Add Entry")],
        [simpleGui.Button("View an FSG ID")],
        [simpleGui.Button("Update a Container Description")],
        [simpleGui.Button("Update a Storage Location")],
        [simpleGui.Button("Update a sample's quantity")],
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


def layout_get_product_quantity():
    layout = [
        [simpleGui.Text(f"Please enter the product's quantity")],
        [simpleGui.Text("Quantity: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), simpleGui.Cancel()]
    ]
    return layout


def layout_view_sample_info(fsg_id):
    layout = [
        [simpleGui.Text(f"FSG ID is: {fsg_id[0]}")],
        [simpleGui.Text(f"Product is: {fsg_id[1]}")],
        [simpleGui.Text(f"Storage Location is: {fsg_id[2]}")],
        [simpleGui.Text(f"Description of container is: {fsg_id[3]}")],
        [simpleGui.Text(f"{fsg_id[4]} {fsg_id[5]}")]
    ]
    return layout
