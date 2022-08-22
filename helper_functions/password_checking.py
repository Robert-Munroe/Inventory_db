from datetime import datetime, date

from helper_functions import special_characters


def password_complexity_check(password: str):
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
    current_time = datetime.now()
    current_year = int(current_time.strftime('%Y'))
    current_month = int(current_time.strftime('%m'))
    current_day = int(current_time.strftime('%d'))

    date_val = date(current_year, current_month, current_day)
    day_of_year = date_val.strftime('%j')

    current_year = int(current_time.strftime('%y'))
    current_year = current_year * 1000

    timestamp = current_year + int(day_of_year)

    return timestamp


def password_expired(timestamp):
    timestamp_difference = timestamp - create_password_time_stamp()
    return timestamp_difference
