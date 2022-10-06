import re
from database_dir import database, storage_locations


def is_product_id_formatted_correctly(product_id):
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    if type(product_id) != str:
        return 1

    new_product = product_id.replace("s", "S")
    new_product = new_product.replace("r", "R")
    match = re.match("[0-9][0-9][S,R][0-9][0-9][0-9][0-9]", new_product)
    is_match = bool(match)
    if not is_match:
        return 1

    if len(product_id) != 7:
        return 1

    if database.does_fsg_id_exist(db_cursor, new_product):
        return 1
    return 0


def is_product_id_formatted_correctly_allow_duplicate(product_id):
    if type(product_id) != str:
        return 1

    new_product = product_id.replace("s", "S")
    new_product = new_product.replace("r", "R")

    match = re.match("[0-9][0-9][S,R][0-9][0-9][0-9][0-9]", new_product)
    is_match = bool(match)
    if not is_match:
        return 1

    if len(product_id) != 7:
        return 1
    return 0


def is_fsg_id_correct(fsg_id):
    is_error = is_product_id_formatted_correctly(fsg_id)
    if is_error == 1:
        return False, "FSG ID is invalid or blank, "
    else:
        return True, ""


def is_storage_location_correct(storage_location):
    acceptable_locations = storage_locations.set_acceptable_locations()
    if storage_location not in acceptable_locations:
        return False, "Storage location is not a valid location, "
    else:
        return True, ""


def is_quantity_correct(quantity):
    if quantity is None:
        quantity = 'a'
    test_quantity = quantity.lstrip('-').replace('.', '', 1).replace('e-', '', 1).replace('e', '', 1)
    if quantity == "" or not test_quantity.isdigit():
        return False, "Quantity is not set or not a valid number, "
    else:
        return True, ""


def is_unit_correct(unit):
    acceptable_units = ["g", "ml", "container(s)", "bag(s)", "vial(s)"]
    if unit not in acceptable_units:
        return False, "entry's units are invalid"
    else:
        return True, ""


def is_storage_type_correct(storage_type):
    acceptable_types = ['RETAIN', 'STABILITY', 'ANALYTICAL']
    if storage_type not in acceptable_types:
        return False, "Storage type is invalid, "
    else:
        return True, ""


def is_storage_position_correct(storage_position):
    acceptable_storage_positions = storage_locations.set_acceptable_storage_positions()
    if storage_position not in acceptable_storage_positions:
        return False, "Storage position is invalid, "
    else:
        return True, ""


def is_entry_correct(fsg_id: str, storage_type, general_id, storage_position, client_id, storage_location,
                     addition_location_one, addition_location_two, description, quantity, unit):
    error_list = ""
    state, statement = is_fsg_id_correct(fsg_id)
    if not state:
        error_list = error_list + statement

    state, statement = is_storage_type_correct(storage_type)
    if not state:
        error_list = error_list + statement

    if general_id == "":
        error_list = error_list + "Product ID is blank, "

    state, statement = is_storage_position_correct(storage_position)
    if not state:
        error_list = error_list + statement

    if client_id == "":
        error_list = error_list + "Client ID is blank, "

    state, statement = is_storage_location_correct(storage_location)
    if not state:
        error_list = error_list + statement

    acceptable_locations_with_na = storage_locations.set_acceptable_locations_with_na()
    if addition_location_one not in acceptable_locations_with_na:
        error_list = error_list + "Addition storage location one is invalid, "

    if addition_location_two not in acceptable_locations_with_na:
        error_list = error_list + "Addition storage location two is invalid, "

    if description == "":
        error_list = error_list + "Description is blank, "

    state, statement = is_quantity_correct(quantity)
    if not state:
        error_list = error_list + statement

    state, statement = is_unit_correct(unit)
    if not state:
        error_list = error_list + statement

    return error_list


def force_caps(user_input: str):
    user_input = user_input.upper()
    return user_input
