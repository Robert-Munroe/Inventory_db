import database
import typechecking


def ask_for_product_id():
    product_id = input("Please enter the product ID")
    is_error = typechecking.is_product_id_formatted_correctly(product_id)
    while is_error == 1:
        product_id = input("Please enter product ID in this format [last two of year ##][S,R][ID CODE ####]")
        is_error = typechecking.is_product_id_formatted_correctly(product_id)
    return product_id


def ask_for_client_id():
    client_id = input("Please enter the client's id code")
    correct = 0
    while correct == 0:
        correct = int(input("Is this the correct client id code " + client_id + "? If yes, press 1, if not press 2."))
        if correct == 2:
            client_id = input("Please enter the client's id code")
            correct = 0
    return client_id


def ask_for_general_id():
    general_id = input("What is the product in general?")
    return general_id


def ask_for_container_number():
    container_count = input("How many containers were present when received?")
    return container_count


def ask_for_product_acquisition():
    date = input("When did we recieve this product?")
    is_error = typechecking.is_product_date_formatted_correctly(date)
    while is_error == 1:
        date = input("Please enter the data in this format [##/##/####]")
        is_error = typechecking.is_product_date_formatted_correctly(date)
    return date


def ask_for_holding_location():
    holding_location = input("Please input holding location")
    return holding_location


def ask_for_description():
    description = input("Please describe the container of this product")
    return description


def build_entry():
    product_id = ask_for_product_id()
    client_id = ask_for_client_id()
    general_id = ask_for_general_id()
    current_container = ask_for_container_number()
    date_received = ask_for_product_acquisition()
    holding_location = ask_for_holding_location()
    description = ask_for_description()
    entry_list = [product_id, client_id, general_id, current_container, current_container, date_received,
                  holding_location, "in", description]
    return entry_list
