import re
from database_dir import database


def is_product_date_formatted_correctly(date):
    if type(date) == str:
        match = re.match("[0-9][0-9][/][0-9][0-9][/][0-9][0-9][0-9][0-9]", date)
        is_match = bool(match)
        if is_match:
            if len(date) == 10:
                return 0
            else:
                return 1
        else:
            return 1
    else:
        return 1


def is_product_id_formatted_correctly(product_id):
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    if type(product_id) != str:
        return 1

    new_product = product_id.replace("s", "S")
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

    match = re.match("[0-9][0-9][S,R][0-9][0-9][0-9][0-9]", new_product)
    is_match = bool(match)
    if not is_match:
        return 1

    if len(product_id) != 7:
        return 1
    return 0


def is_entry_correct(product_id, general_id, holding_location, description, quantity, unit):
    acceptable_units = ["g", "ml", "container(s)", "bag(s)", "vial(s)"]
    test_quantity = quantity.lstrip('-').replace('.', '', 1).replace('e-', '', 1).replace('e', '', 1)
    is_error = is_product_id_formatted_correctly(product_id)

    if is_error == 1 or general_id == "" or holding_location == "" or description == "" or quantity == "" or \
            unit not in acceptable_units or test_quantity.isdigit() == False:
        error_list = []
        if is_error == 1:
            error_list.append(1)
        if general_id == "":
            error_list.append(2)
        if holding_location == "":
            error_list.append(3)
        if description == "":
            error_list.append(4)
        if quantity == "" or test_quantity.isdigit() == False:
            error_list.append(5)
        if unit not in acceptable_units:
            error_list.append(6)
        return error_list
