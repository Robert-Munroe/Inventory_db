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
