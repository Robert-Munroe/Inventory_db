from helper_functions import typechecking


def count_case(user_input, output):
    count_lower_case = 0
    count_upper_case = 0
    for character in user_input:
        if character.islower():
            count_lower_case += 1
    for character in output:
        if character.isupper():
            count_upper_case += 1
    return count_lower_case, count_upper_case


def test_force_caps():
    test_string = "i'm a test"
    output = typechecking.force_caps(test_string)
    assert output == "I'M A TEST"
    assert len(output) == 10

    count_lower_case, count_upper_case = count_case(test_string, output)

    assert count_lower_case == 7
    assert count_lower_case == count_upper_case

    count_lower_case, count_upper_case = count_case("1234123412341234", typechecking.force_caps("1234123412341234"))
    assert count_lower_case == count_upper_case

    count_lower_case, count_upper_case = count_case("", typechecking.force_caps(""))
    assert count_lower_case == count_upper_case

    count_lower_case, count_upper_case = count_case("$%$%", typechecking.force_caps("$%$%"))
    assert count_lower_case == count_upper_case


def test_is_product_id_formatted_correctly_duplicate():
    test_id = '21s0001'
    is_error = typechecking.is_product_id_formatted_correctly_allow_duplicate(test_id)
    assert is_error == 0

    test_id = '21S0001'
    is_error = typechecking.is_product_id_formatted_correctly_allow_duplicate(test_id)
    assert is_error == 0

    test_id = '21r0001'
    is_error = typechecking.is_product_id_formatted_correctly_allow_duplicate(test_id)
    assert is_error == 0

    test_id = '21R0001'
    is_error = typechecking.is_product_id_formatted_correctly_allow_duplicate(test_id)
    assert is_error == 0

    test_id = ''
    is_error = typechecking.is_product_id_formatted_correctly_allow_duplicate(test_id)
    assert is_error == 1

    test_id = '21S00011'
    is_error = typechecking.is_product_id_formatted_correctly_allow_duplicate(test_id)
    assert is_error == 1

    test_id = '211S0001'
    is_error = typechecking.is_product_id_formatted_correctly_allow_duplicate(test_id)
    assert is_error == 1

    test_id = '2140001'
    is_error = typechecking.is_product_id_formatted_correctly_allow_duplicate(test_id)
    assert is_error == 1


def test_correct_entry():
    fsg_id = "10s0001"  # not in database
    general_id = 'water'
    client_id = 'client 0003'
    holding_location = "F7R1S1BA"
    description = 'Clear Glass Jar'
    quantity = '5'
    unit = 'g'
    message = typechecking.is_entry_correct(fsg_id, general_id, client_id, holding_location, description, quantity,
                                            unit)
    assert message == ''

    message = typechecking.is_entry_correct("", general_id, client_id, holding_location, description, quantity, unit)
    assert message == "FSG ID is invalid or blank, "

    message = typechecking.is_entry_correct("", "", client_id, holding_location, description, quantity, unit)
    assert message == "FSG ID is invalid or blank, Product ID is blank, "

    message = typechecking.is_entry_correct("", "", "", holding_location, description, quantity, unit)
    assert message == "FSG ID is invalid or blank, Product ID is blank, Client ID is blank, "

    message = typechecking.is_entry_correct("", "", "", "", description, quantity, unit)
    assert message == "FSG ID is invalid or blank, Product ID is blank, Client ID is blank, " \
                      "Storage location is not a valid location, "

    message = typechecking.is_entry_correct("", "", "", "", "", quantity, unit)
    assert message == "FSG ID is invalid or blank, Product ID is blank, Client ID is blank," \
                      " Storage location is not a valid location, Description is blank, "

    message = typechecking.is_entry_correct("", "", "", "", "", "", unit)
    assert message == "FSG ID is invalid or blank, Product ID is blank, Client ID is blank," \
                      " Storage location is not a valid location, Description is blank," \
                      " Quantity is not set or not a valid number, "

    message = typechecking.is_entry_correct("", "", "", "", "", "", "")
    assert message == "FSG ID is invalid or blank, Product ID is blank, Client ID is blank," \
                      " Storage location is not a valid location, Description is blank," \
                      " Quantity is not set or not a valid number, entry's units are invalid"

    message = typechecking.is_entry_correct("21s0001", general_id, client_id, holding_location, description, quantity,
                                            unit)
    assert message == 'FSG ID is invalid or blank, '
