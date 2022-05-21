import database
import gui


def main():
    connection, db_cursor = database.open_db("foundersinventorydb.sqlite")
    database.create_table(db_cursor)
    gui.main_window()


if __name__ == '__main__':
    main()
