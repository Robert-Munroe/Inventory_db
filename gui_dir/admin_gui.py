import PySimpleGUI as simpleGui

from database_dir import database, log_in_database_functions
from gui_dir import user_layouts, admin_windows, gui_windows, logging_gui_buttons
from helper_functions import password_checking


def admin_main_window():
    layout = user_layouts.layout_admin_window()

    window = simpleGui.Window("Founders Database Admin", layout, element_justification='l')

    while True:
        event, values = window.read()
        if event == "Add User":
            add_user_button()
        if event == "Edit User":
            edit_a_user()
        if event == "Print User Log":
            print_user_log()
        if event == "Exit" or event == simpleGui.WINDOW_CLOSED:
            break
    window.close()


def db_connection_and_cursor():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    return connection, db_cursor


def add_user_button():
    connection, db_cursor = db_connection_and_cursor()
    user_name, password, initials = admin_windows.add_user_window()

    error_list = ""
    if user_name == "":
        error_list = error_list + "user name is empty"
    else:
        duplicate_user_check = log_in_database_functions.duplicate_user_check(db_cursor, user_name)
        if duplicate_user_check:
            error_list = error_list + "user name is in use"

    if password == "":
        error_list = error_list + " password is empty"
    if initials == "":
        error_list = error_list + " initials are empty"

    password_length_flag, upper_case_flag, lower_case_flag, special_character_flag, number_flag = \
        password_checking.password_complexity_check(password)

    if not password_length_flag and len(password) > 0:
        gui_windows.pop_up_window("Error", "Password needs to be longer")
        return

    complexity_count = upper_case_flag + lower_case_flag + special_character_flag + number_flag

    if complexity_count < 3 and len(password) > 0:
        gui_windows.pop_up_window("Error", "Password needs to be more complex")
        return

    if len(error_list) > 0:
        gui_windows.pop_up_window("Error", error_list)
        return

    timestamp = password_checking.create_password_time_stamp()

    password_history = " n/a," + "n/a," + f"{password}"
    user = [user_name, password, initials, timestamp, password_history]
    log_in_database_functions.insert_into_user_table(db_cursor, connection, user)


def edit_a_user():
    connection, db_cursor = db_connection_and_cursor()
    user_name = admin_windows.get_user()
    does_user_exist = log_in_database_functions.user_exist(db_cursor, user_name)

    if not does_user_exist:
        gui_windows.pop_up_window("Error", "User does not exist")
        return

    if user_name == "SYSADMIN":
        gui_windows.pop_up_window("Error", "You cannot change admin password this way")
        return

    password, timestamp = admin_windows.get_change_user_password(user_name)

    if not password:
        gui_windows.pop_up_window("Error", "Password is blank")
        return

    password_length_flag, upper_case_flag, lower_case_flag, special_character_flag, number_flag = \
        password_checking.password_complexity_check(password)

    if not password_length_flag and len(password) > 0:
        gui_windows.pop_up_window("Error", "Password needs to be longer")
        return

    complexity_count = upper_case_flag + lower_case_flag + special_character_flag + number_flag

    if complexity_count < 3 and len(password) > 0:
        gui_windows.pop_up_window("Error", "Password needs to be more complex")
        return

    currently_used_passwords = log_in_database_functions.get_password_history(db_cursor, user_name)
    current_password_history = password_checking.build_password_list(currently_used_passwords)
    is_password_repeated = password_checking.check_password_history(current_password_history, password)

    if is_password_repeated:
        gui_windows.pop_up_window("Error", "Password previously used")
        return

    updated_password_list = password_checking.build_password_history(currently_used_passwords, password)

    log_in_database_functions.change_user_password(db_cursor, connection, user_name, password, timestamp,
                                                   updated_password_list)
    gui_windows.pop_up_window("Success", "Password changed")


def print_user_log():
    connection, db_cursor = db_connection_and_cursor()
    list_of_users = log_in_database_functions.get_all_users(db_cursor)
    file_header = set_file_header()
    if not list_of_users:
        gui_windows.pop_up_window('error', 'no users')
    list_entries_lists = [list(i) for i in list_of_users]
    list_entries_lists = [file_header] + list_entries_lists

    with open('list_of_users_temp.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)

    logging_gui_buttons.file_formatter('list_of_users_temp', 'List_of_users')


def set_file_header():
    file_header = ['Username', 'Password', 'Initials', 'Time of password', 'List of previous 3 passwords']
    return file_header
