import PySimpleGUI as simpleGui


def layout_main_window():
    layout = [
        [simpleGui.Text("Please enter your user name")],
        [simpleGui.Text("User name: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("Please enter your password")],
        [simpleGui.Text("Password: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), simpleGui.Cancel()]
    ]
    return layout


def layout_admin_window():
    layout = [
        [simpleGui.Text("Welcome Admin")],
        [simpleGui.Button("Add User")],
        [simpleGui.Button("Edit User")],
        [simpleGui.Button("Print User Log")],
        [simpleGui.Button("Exit")]
    ]
    return layout


def layout_user_details():
    layout = [
        [simpleGui.Text("Please enter a unique user name")],
        [simpleGui.Text("Username: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("Please enter a password")],
        [simpleGui.Text("Password: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Text("Please enter a the employee's initials")],
        [simpleGui.Text("Initials:", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), simpleGui.Cancel()]
    ]
    return layout


def layout_get_user_name():
    layout = [
        [simpleGui.Text("Please enter a user name")],
        [simpleGui.Text("Username: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), simpleGui.Cancel()]
    ]
    return layout


def layout_change_user_password():
    layout = [
        [simpleGui.Text("Please enter a password")],
        [simpleGui.Text("Password: ", size=(15, 1)), simpleGui.InputText()],
        [simpleGui.Submit(), simpleGui.Cancel()]
    ]
    return layout
