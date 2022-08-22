import PySimpleGUI as simpleGui

from gui_dir import user_layouts


def main_user_window():
    layout = user_layouts.layout_main_window()
    window = simpleGui.Window("Founders Database Log In", layout)

    while True:
        event, values = window.read()
        if event == "Cancel":
            window.close()
            user_name = ""
            password = ""
            return user_name, password
        if event == "Submit":
            user_name = values[0]
            password = values['Password']
            window.close()
            return user_name, password
        window.close()
        user_name = ""
        password = ""
        return user_name, password
