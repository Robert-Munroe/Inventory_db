import database
import entrybuilder
import gui
import gui_windows


def main():
    connection, db_cursor = database.open_db("foundersinventorydb.sqlite")
    database.create_table(db_cursor)
    layout = gui_windows.get_layout_main_window()

    window = gui.simpleGui.Window("Founders Database", layout)

    while True:
        event, values = window.read()
        if event == "Add Entry":
            gui.add_entry_button()
        if event == "View an FSG ID":
            gui.view_a_sample_button()
        if event == "Update a Container Description":
            gui.update_a_description_button()
        if event == "Update a Storage Location":
            gui.update_a_holding_location_button()
        if event == "Exit" or event == gui.simpleGui.WINDOW_CLOSED:
            break
    window.close()


if __name__ == '__main__':
    main()
