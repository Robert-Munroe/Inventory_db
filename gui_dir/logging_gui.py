import PySimpleGUI as simpleGui
from gui_dir import layouts, logging_gui_buttons


def logging_main_window():
    layout = layouts.layout_logging_main_window()

    window = simpleGui.Window("Founders Database Logging", layout)

    while True:
        event, values = window.read()
        if event == "FSG_ID with X Product Name":
            fsg_id_by_product_name_button()
        if event == "Historic FSG_ID with X Product Name":
            fsg_id_by_product_name_button_historic()
        if event == "Samples in storage location":
            storage_location_dump()
        if event == "Historic FSG_ID in storage location":
            storage_location_dump_historic()
        if event == "Exit" or event == simpleGui.WINDOW_CLOSED:
            break
    window.close()


def fsg_id_by_product_name_button():
    logging_gui_buttons.fsg_by_product_name()


def fsg_id_by_product_name_button_historic():
    logging_gui_buttons.fsg_by_product_name_historic()


def storage_location_dump():
    return


def storage_location_dump_historic():
    return