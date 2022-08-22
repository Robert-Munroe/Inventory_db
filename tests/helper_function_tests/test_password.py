from helper_functions import password_checking
from datetime import datetime, date


def test_password_complexity():
    known_password_not_complex = 'password'
    password_length_flag, upper_case_flag, lower_case_flag, special_character_flag, number_flag = \
        password_checking.password_complexity_check(known_password_not_complex)

    complexity_sum = upper_case_flag + lower_case_flag + special_character_flag + number_flag

    assert password_length_flag
    assert complexity_sum == 1
    assert upper_case_flag == 0
    assert lower_case_flag == 1
    assert number_flag == 0
    assert special_character_flag == 0

    known_password_not_complex = 'pa55wo'

    password_length_flag, upper_case_flag, lower_case_flag, special_character_flag, number_flag = \
        password_checking.password_complexity_check(known_password_not_complex)

    complexity_sum = upper_case_flag + lower_case_flag + special_character_flag + number_flag

    assert not password_length_flag
    assert complexity_sum == 2
    assert lower_case_flag == 1
    assert number_flag == 1
    assert upper_case_flag == 0
    assert special_character_flag == 0

    known_password_is_complex = 'pa55wo$$'

    password_length_flag, upper_case_flag, lower_case_flag, special_character_flag, number_flag = \
        password_checking.password_complexity_check(known_password_is_complex)

    assert password_length_flag
    assert upper_case_flag == 0
    assert lower_case_flag == 1
    assert special_character_flag == 1
    assert number_flag == 1

    known_password_not_complex = ""
    password_length_flag, upper_case_flag, lower_case_flag, special_character_flag, number_flag = \
        password_checking.password_complexity_check(known_password_not_complex)

    assert not password_length_flag
    assert upper_case_flag == 0
    assert lower_case_flag == 0
    assert special_character_flag == 0
    assert number_flag == 0


def test_time_generation():
    function_timestamp = password_checking.create_password_time_stamp()
    assert type(function_timestamp) is int

    year = datetime.now()
    current_year = int(year.strftime('%y'))

    function_year = function_timestamp//1000

    assert function_year == current_year

    current_time = datetime.now()
    current_month = int(current_time.strftime('%m'))
    current_day = int(current_time.strftime('%d'))
    current_year = int(current_time.strftime('%Y'))

    date_val = date(current_year, current_month, current_day)
    day_of_year = date_val.strftime('%j')

    assert function_timestamp % 1000 == int(day_of_year)
