from database_dir import database
from gui_dir import gui


def main():
    connection, db_cursor = database.open_db("database_dir/foundersinventorydb.sqlite")
    database.create_table(db_cursor)
    gui.main_window()


if __name__ == '__main__':
    main()
