import datetime
from helper_functions import special_characters


def password_complexity_check(password):
    password_length_flag = False
    if len(password) >= 7:
        password_length_flag = True

    upper_case_flag = 0
    for character in password:
        if character.isupper():
            upper_case_flag = 1
            break

    lower_case_flag = 0
    for character in password:
        if character.islower():
            lower_case_flag = 1
            break

    acceptable_special_characters = special_characters.set_special_characters()
    special_character_flag = 0
    for character in password:
        if character in acceptable_special_characters:
            special_character_flag = 1
            break

    number_flag = 0
    for character in password:
        if character.isdigit():
            number_flag = 1
            break

    return password_length_flag, upper_case_flag, lower_case_flag, special_character_flag, number_flag
