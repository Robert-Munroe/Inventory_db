import typechecking
import gui_windows


def ask_for_product_id_allow_duplicate():
    product_id = gui_windows.get_fsg_id()
    is_error = typechecking.is_product_id_formatted_correctly_allow_duplicate(product_id)
    if is_error != 0:
        return
    return product_id


def ask_for_product_id():
    product_id = gui_windows.get_fsg_id()
    is_error = typechecking.is_product_id_formatted_correctly(product_id)
    while is_error == 1:
        product_id = gui_windows.get_fsg_id()
        is_error = typechecking.is_product_id_formatted_correctly(product_id)
    return product_id


def ask_for_contents():
    contents = input("How would you like to measure this product?\nWould you like to measure this in grams, volume"
                     ", or in containers?")
    number_of_contents = input("How many " + contents + " exist?")

    return contents, number_of_contents


def build_entry(product_id, general_id, holding_location, description):
    entry_list = [product_id, general_id, holding_location, description]
    return entry_list
