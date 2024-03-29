import PySimpleGUI as simpleGui

from gui_dir import user_layouts
from helper_functions import password_checking, typechecking


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
            user_name = typechecking.force_caps(user_name)
            password = values[1]
            initials = values[2]
            initials = typechecking.force_caps(initials)
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
            user_name = typechecking.force_caps(user_name)
            window.close()
            return user_name
        user_name = ""
        window.close()
        return user_name


def get_change_user_password(username):
    layout = user_layouts.layout_change_user_password()
    window = simpleGui.Window(f"{username}", layout)
    while True:
        event, values = window.read()
        if event == "Cancel":
            window.close()
            password = ""
            timestamp = ""
            return password, timestamp
        if event == "Submit":
            password = values[0]
            timestamp = password_checking.create_password_time_stamp()
            window.Close()
            return password, timestamp
        window.close()
        password = ""
        timestamp = ""
        return password, timestamp

