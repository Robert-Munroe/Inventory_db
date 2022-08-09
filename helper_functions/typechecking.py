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

    if database.get_product_id_from_db(db_cursor, new_product) != 0:
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


def is_entry_correct(product_id, general_id, client_id, holding_location, description, quantity, unit,
                     fsg_id_event_log):
    acceptable_units = ["g", "ml", "container(s)", "bag(s)", "vial(s)"]
    acceptable_locations = storage_locations.set_acceptable_locations()
    if quantity is None:
        quantity = 'a'
    test_quantity = quantity.lstrip('-').replace('.', '', 1).replace('e-', '', 1).replace('e', '', 1)
    is_error = is_product_id_formatted_correctly(product_id)

    if is_error == 1 or general_id == "" or client_id == "" or holding_location == "" or \
            holding_location not in acceptable_locations or description == "" or quantity == "" \
            or unit not in acceptable_units or test_quantity.isdigit() or fsg_id_event_log == "" == False:
        error_list = ""
        if is_error == 1:
            error_list = error_list + "FSG ID is invalid or blank,"
        if general_id == "":
            error_list = error_list + "product field is blank,"
        if client_id == "":
            error_list = error_list + "the client ID is blank,"
        if holding_location == "":
            error_list = error_list + "storage location is blank,"
        if holding_location not in acceptable_locations:
            error_list = error_list + "storage location is invalid,"
        if description == "":
            error_list = error_list + "container description is blank,"
        if quantity == "" or test_quantity.isdigit() == False:
            error_list = error_list + "product's quantity is not set, or not a valid number,"
        if unit not in acceptable_units:
            error_list = error_list + "product's units are invalid or not set,"
        return error_list


def force_caps(user_input: str):
    user_input = user_input.upper()
    return user_input
