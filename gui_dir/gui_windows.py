from datetime import datetime

import PySimpleGUI as simpleGui

from gui_dir import layouts
from helper_functions import typechecking


def pop_up_window(window_type, attribute):
    layout = layouts.layout_pop_up_window(attribute)
    window = simpleGui.Window(window_type, layout)
    while_pop_up_window_is_true_loop(window)


def while_pop_up_window_is_true_loop(window):
    while True:
        event, values = window.read()
        if event == simpleGui.WINDOW_CLOSED:
            break


def get_entry_details(initials):
    layout = layouts.layout_entry_details()
    window = simpleGui.Window("Add an Entry", layout)
    current_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    while True:
        event, values = window.read()
        if event == "Cancel":
            window.close()
            fsg_id = "error"
            storage_type = ""
            product_id = ""
            client_id = ""
            storage_location = ""
            container_description = ""
            quantity = ""
            aggregate_form = ""
            fsg_id_event_log = ""
            return fsg_id, storage_type, product_id, client_id, storage_location, container_description, quantity, \
                aggregate_form, fsg_id_event_log

        if event == "Submit":
            fsg_id = values[0]
            fsg_id = fsg_id.replace("s", "S")
            storage_type = values[1]
            storage_type = typechecking.force_caps(storage_type)
            product_id = values[2]
            product_id = typechecking.force_caps(product_id)
            client_id = values[3]
            client_id = typechecking.force_caps(client_id)
            storage_location = values[4]
            storage_location = typechecking.force_caps(storage_location)
            container_description = values[5]
            quantity = values[6]
            aggregate_form = values[7]
            fsg_id_event_log = \
                current_time + " " + initials + " " + str(values[6]) + " " + values[7] + " " + " FSG ID created,"
            window.close()
            return fsg_id, storage_type, product_id, client_id, storage_location, container_description, quantity,\
                aggregate_form, fsg_id_event_log
        fsg_id = "error"
        storage_type = ""
        product_id = ""
        client_id = ""
        storage_location = ""
        container_description = ""
        quantity = ""
        aggregate_form = ""
        fsg_id_event_log = ""
        window.close()
        return fsg_id, storage_type, product_id, client_id, storage_location, container_description, quantity, \
            aggregate_form, fsg_id_event_log


def invalid_entry_window(error_list):
    error_text = error_list

    error_text = error_text + "\nyour actions were not logged"
    error_text = error_text.replace(",", "\n")

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


def get_update_entry(fsg_id, storage_type, storage_location, description, quantity, form, initials):
    layout = layouts.layout_get_entry_update(fsg_id, storage_location, storage_type, description, quantity)
    window = simpleGui.Window(f"Change {fsg_id}", layout)
    current_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    while True:
        event, values = window.read()
        if event == "Cancel":
            storage_location = ""
            storage_type = ""
            description = ""
            quantity = ""
            reason_for_change = ""
            window.close()
            return storage_location, storage_type, description, quantity, reason_for_change
        if event == "Submit":
            storage_location = values[0]
            storage_location = typechecking.force_caps(storage_location)
            storage_type = values[1]
            storage_type = typechecking.force_caps(storage_type)
            description = values[2]
            quantity = values[3]
            edit_reason = values[4]
            reason_for_change = \
                current_time + " " + initials + " " + str(values[3]) + " " + form + " " + \
                edit_reason.replace(",", "") + ","
            window.Close()
            return storage_location, storage_type, description, quantity, reason_for_change
        window.close()
        storage_location = ""
        storage_type = ""
        description = ""
        quantity = ""
        reason_for_change = ""
        return storage_location, storage_type, description, quantity, reason_for_change


def view_a_sample_window(product_info):
    if not product_info:
        pop_up_window("Error", "Entry is invalid")
        return

    if product_info:
        layout_for_valid_entry = layouts.layout_view_sample_info(product_info)

        window = simpleGui.Window(f"Entry of {product_info[0]}", layout_for_valid_entry)
        while_pop_up_window_is_true_loop(window)


def get_product_id():
    layout = layouts.layout_get_product_id()
    window = simpleGui.Window("Enter product id", layout)
    while True:
        event, values = window.read()
        if event == "Cancel":
            window.close()
            return
        if event == "Submit":
            product_id = values[0]
            product_id = typechecking.force_caps(product_id)
            window.close()
            return product_id
        window.close()
        return


def get_storage_location():
    layout = layouts.layout_get_storage_location()
    window = simpleGui.Window("Enter a storage location", layout)
    while True:
        event, values = window.read()
        if event == "Cancel":
            window.close()
            return
        if event == "Submit":
            storage_location = values[0]
            storage_location = typechecking.force_caps(storage_location)
            window.close()
            return storage_location
        window.close()
        return


def get_client_id():
    layout = layouts.layout_get_client_id()
    window = simpleGui.Window("Enter client id", layout)
    while True:
        event, values = window.read()
        if event == "Cancel":
            window.close()
            return
        if event == "Submit":
            client_id = values[0]
            client_id = typechecking.force_caps(client_id)
            window.close()
            return client_id
        window.close()
        return
