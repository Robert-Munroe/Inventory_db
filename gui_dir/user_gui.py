import PySimpleGUI as simpleGui
from gui_dir import user_layouts, gui_windows
from database_dir import database
from helper_functions import typechecking


def main_user_window():
    layout = user_layouts.layout_main_window()
    window = simpleGui.Window("Founders Database Log In", layout)

    while True:
        event, values = window.read()
        if event == "Cancel":
            window.close()
            return
        if event == "Submit":
            user_name = values[0]
            password = values[1]
            window.close()
            return user_name, password
        window.close()
        user_name = ""
        password = ""
        return user_name, password

