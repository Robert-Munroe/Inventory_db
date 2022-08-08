from datetime import datetime
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


def create_password_time_stamp():

    year = datetime.now()
    current_year = int(year.strftime('%y'))
    month = datetime.now()
    current_month = int(month.strftime('%m'))
    day = datetime.now()
    current_day = int(day.strftime('%d'))

    current_year = current_year % 2000
    current_year = current_year * 1000
    current_month = (current_month-1) * 30

    timestamp = current_day + current_month + current_year

    return timestamp


