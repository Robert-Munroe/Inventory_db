from database_dir import database
from gui_dir import gui, user_gui


def main():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    database.create_table(db_cursor)

    user_name, password = user_gui.main_user_window()
    can_continue = database.get_log_in_from_db(db_cursor, user_name, password)
    if can_continue == 1:
        gui.main_window()


if __name__ == '__main__':
    main()
