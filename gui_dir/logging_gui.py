import PySimpleGUI as simpleGui
from gui_dir import layouts, logging_gui_buttons


def logging_main_window():
    layout = layouts.layout_logging_main_window()

    window = simpleGui.Window("Founders Database Logging", layout)

    while True:
        event, values = window.read()
        if event == "FSG_ID by Product Name":
            fsg_id_by_product_name_button()
        if event == "Historic FSG_ID by Product Name":
            fsg_id_by_product_name_button_historic()
        if event == "FSG_ID in Storage Location":
            storage_location_dump()
        if event == "Historic FSG_ID in Storage Location":
            storage_location_dump_historic()
        if event == "FSG_ID by client":
            fsg_id_by_client_button()
        if event == "Historic FSG_ID by client":
            fsg_id_by_client_historic_button()
        if event == "History of FSG_ID":
            fsg_id_dump()
        if event == "Exit" or event == simpleGui.WINDOW_CLOSED:
            break
    window.close()


def fsg_id_by_product_name_button():
    logging_gui_buttons.fsg_by_product_name()


def fsg_id_by_product_name_button_historic():
    logging_gui_buttons.fsg_by_product_name_historic()


def storage_location_dump():
    logging_gui_buttons.get_fsg_id_from_storage_location()


def storage_location_dump_historic():
    logging_gui_buttons.get_fsg_id_from_storage_location_historic()


def fsg_id_by_client_button():
    logging_gui_buttons.get_fsg_id_by_client()


def fsg_id_by_client_historic_button():
    logging_gui_buttons.get_fsg_id_by_client_historic()


def fsg_id_dump():
    logging_gui_buttons.fsg_id_dump_button()
