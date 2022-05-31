from database_dir import database
from gui_dir import gui


def main():
    location_of_db = database.db_location()
    connection, db_cursor = database.open_db(location_of_db)
    database.create_table(db_cursor)
    gui.main_window()


if __name__ == '__main__':
    main()
