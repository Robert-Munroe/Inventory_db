from helper_functions import typechecking


def ask_for_fsg_id_allow_duplicate(fsg_id):
    is_error = typechecking.is_product_id_formatted_correctly_allow_duplicate(fsg_id)
    if is_error != 0:
        return
    new_fsg_id = fsg_id.replace("s", "S")
    new_fsg_id = new_fsg_id.replace("r", "R")
    return new_fsg_id
