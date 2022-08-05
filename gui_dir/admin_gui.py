import PySimpleGUI as simpleGui
from gui_dir import user_layouts, admin_windows, gui_windows
from database_dir import database, log_in_database_functions


def admin_main_window():
    layout = user_layouts.layout_admin_window()

    window = simpleGui.Window("Founders Database Admin", layout)

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


def add_user_button():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
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

    if len(error_list) > 0:
        gui_windows.pop_up_window("Error", error_list)
        return

    user = [user_name, password, initials]
    print("put in table")
    log_in_database_functions.insert_into_user_table(db_cursor,connection, user)


def edit_a_user():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)

    user_name = admin_windows.get_user()
    does_user_exist = log_in_database_functions.user_exist(db_cursor, user_name)

    if not does_user_exist:
        gui_windows.pop_up_window("Error", "User does not exist")
        return

    if user_name == "SYSADMIN":
        gui_windows.pop_up_window("Error", "You cannot change admin password this way")
        return

    password = admin_windows.get_change_user_password(user_name)

    if not password:
        gui_windows.pop_up_window("Error", "Password is blank")
        return

    log_in_database_functions.change_user_password(db_cursor, connection, user_name, password)
    gui_windows.pop_up_window("Success", "Password changed")


def print_user_log():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    list_of_users = log_in_database_functions.get_all_users(db_cursor)
    if not list_of_users:
        gui_windows.pop_up_window('error', 'no users')
    list_entries_lists = [list(i) for i in list_of_users]

    with open('list_of_users.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)
