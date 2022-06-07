from helper_functions import typechecking
from gui_dir import gui_windows


def ask_for_product_id_allow_duplicate():
    product_id = gui_windows.get_fsg_id()
    is_error = typechecking.is_product_id_formatted_correctly_allow_duplicate(product_id)
    if is_error != 0:
        return
    new_product = product_id.replace("s", "S")
    new_product = new_product.replace("r", "R")
    return new_product


def ask_for_product_id():
    product_id = gui_windows.get_fsg_id()
    is_error = typechecking.is_product_id_formatted_correctly(product_id)
    while is_error == 1:
        product_id = gui_windows.get_fsg_id()
        is_error = typechecking.is_product_id_formatted_correctly(product_id)
    new_product = product_id.replace("s", "S")
    new_product = new_product.replace("r", "R")
    return new_product


def build_entry(product_id, general_id, holding_location, description):
    entry_list = [product_id, general_id, holding_location, description]
    return entry_list
