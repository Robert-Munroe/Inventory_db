from database_dir import database, log_in_database_functions
from gui_dir import gui, login_gui, admin_gui
from helper_functions import password_checking, typechecking


def main():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    database.create_table(db_cursor)

    user_name, password = login_gui.main_user_window()
    user_name = typechecking.force_caps(user_name)
    logged_in, navigator, timestamp = database.get_log_in_from_db(db_cursor, user_name, password)
    if not timestamp:
        return

    change_password = password_checking.password_expired(timestamp)
    if change_password:
        return

    if logged_in:
        initials = log_in_database_functions.get_user_initials(db_cursor, user_name)
        if navigator == "SYSADMIN":
            admin_gui.admin_main_window()

        if navigator != "SYSADMIN":
            gui.main_window(initials)


if __name__ == '__main__':
    main()
