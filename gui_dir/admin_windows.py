import PySimpleGUI as simpleGui
from gui_dir import user_layouts


def add_user_window():
    layout = user_layouts.layout_user_details()
    window = simpleGui.Window("Add a user", layout)

    while True:
        event, values = window.read()
        if event == "Cancel":
            window.close()
            user_name = ""
            password = ""
            initials = ""
            return user_name, password, initials

        if event == "Submit":
            user_name = values[0]
            password = values[1]
            initials = values[2]
            window.close()
            return user_name, password, initials
        user_name = ""
        password = ""
        initials = ""
        window.close()
        return user_name, password, initials


def get_user():
    layout = user_layouts.layout_get_user_name()
    window = simpleGui.Window("Enter a username", layout)

    while True:
        event, values = window.read()
        if event == "Cancel":
            window.close()
            user_name = ""
            return user_name

        if event == "Submit":
            user_name = values[0]
            window.close()
            return user_name
        user_name = ""
        window.close()
        return user_name


def get_change_user_password(username):
    layout = user_layouts.layout_change_user_password()
    while True:
        window = simpleGui.Window(f"{username}", layout)
        event, values = window.read()
        if event == "Cancel":
            window.close()
            return
        if event == "Submit":
            password = values[0]
            window.Close()
            return password
        window.close()
        return
