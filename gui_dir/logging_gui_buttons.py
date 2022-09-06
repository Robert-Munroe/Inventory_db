from database_dir import logging_functions
import os
from gui_dir import gui_windows


def fsg_by_product_name(product_id, db_cursor):
    list_header = set_file_header()
    list_of_fsg_ids_and_locations = logging_functions.get_locations_of_product_id(product_id, db_cursor)
    if not list_of_fsg_ids_and_locations:
        gui_windows.pop_up_window('error', 'no product_id')
        return
    list_entries_lists = [list(i) for i in list_of_fsg_ids_and_locations]
    list_entries_lists = [list_header] + list_entries_lists
    with open(f'fsg_by_{product_id}_temp.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)
    f.close()
    file_formatter(f'fsg_by_{product_id}_temp', f'fsg_by_{product_id}')


def fsg_by_product_name_historic(product_id, db_cursor):
    list_header = set_file_header()
    list_of_fsg_ids_and_locations = logging_functions.get_locations_of_product_id_historic(product_id, db_cursor)
    if not list_of_fsg_ids_and_locations:
        gui_windows.pop_up_window('error', 'no product_id')
        return
    list_entries_lists = [list(i) for i in list_of_fsg_ids_and_locations]
    list_entries_lists = [list_header] + list_entries_lists

    with open(f'fsg_by_{product_id}_temp.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)
    f.close()
    file_formatter(f'fsg_by_{product_id}_temp', f'fsg_by_{product_id}_historic')


def get_fsg_id_from_storage_location(storage_location, db_cursor):
    list_header = set_file_header()
    list_of_records = logging_functions.get_fsg_id_from_storage_location(storage_location, db_cursor)
    if not list_of_records:
        gui_windows.pop_up_window('error', 'empty storage location')
        return
    list_entries_lists = [list(i) for i in list_of_records]
    list_entries_lists = [list_header] + list_entries_lists

    with open(f'fsg_by_{storage_location}_temp.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)
    f.close()
    file_formatter(f'fsg_by_{storage_location}_temp', f'fsg_by_{storage_location}')


def get_fsg_id_from_storage_location_historic(storage_location, db_cursor):
    list_header = set_file_header()
    list_of_records = logging_functions.get_fsg_id_from_storage_location_historic(storage_location, db_cursor)
    if not list_of_records:
        gui_windows.pop_up_window('error', 'empty storage location')
        return
    list_entries_lists = [list(i) for i in list_of_records]
    list_entries_lists = [list_header] + list_entries_lists

    with open(f'fsg_by_{storage_location}_temp.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)
    f.close()
    file_formatter(f'fsg_by_{storage_location}_temp', f'fsg_by_{storage_location}_historic')


def get_fsg_id_by_client(client, db_cursor):
    list_header = set_file_header()
    list_of_records = logging_functions.get_fsg_id_by_client(client, db_cursor)

    if not list_of_records:
        gui_windows.pop_up_window('error', 'client id has no records')
        return

    list_entries_lists = [list(i) for i in list_of_records]
    list_entries_lists = [list_header] + list_entries_lists

    with open(f'fsg_by_{client}_temp.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)
    f.close()
    file_formatter(f'fsg_by_{client}_temp', f'fsg_by_{client}')


def get_fsg_id_by_client_historic(client, db_cursor):
    list_header = set_file_header()
    list_of_records = logging_functions.get_fsg_id_by_client_historic(client, db_cursor)

    if not list_of_records:
        gui_windows.pop_up_window('error', 'client id has no records')
        return

    list_entries_lists = [list(i) for i in list_of_records]
    list_entries_lists = [list_header] + list_entries_lists

    with open(f'fsg_by_{client}_temp.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)
    f.close()
    file_formatter(f'fsg_by_{client}_temp', f'fsg_by_{client}_historic')


def get_all_entries_historic(cursor):
    list_header = set_file_header()
    list_header.append('Storage_type')
    record = logging_functions.get_all_entries_historic(cursor)
    if not record:
        gui_windows.pop_up_window('Error', 'Database population: you')
        return
    list_entries_lists = [list(i) for i in record]
    list_entries_lists = [list_header] + list_entries_lists

    with open('all_entries_temp.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)
    f.close()
    file_formatter('all_entries_temp', 'all_entries_historic')


def get_all_entries(cursor):
    list_header = set_file_header()
    list_header.append('Storage_type')
    record = logging_functions.get_all_entries(cursor)
    if not record:
        gui_windows.pop_up_window('Error', 'Database population: you')
        return
    list_entries_lists = [list(i) for i in record]
    list_entries_lists = [list_header] + list_entries_lists

    with open('all_entries_temp.txt', 'w') as f:
        for item in list_entries_lists:
            f.write("%s\n" % item)
    f.close()
    file_formatter('all_entries_temp', 'all_entries')


def fsg_id_dump_button(fsg_id, db_cursor):
    # do not use file formatter for this function
    record = logging_functions.get_audit_log_by_fsg_id(fsg_id, db_cursor)

    if not record:
        gui_windows.pop_up_window('Error', 'no FSG ID found')
        return

    list_record = [list(i) for i in record]

    with open(f'audit_log_of_{fsg_id}.txt', 'w') as f:
        for item in list_record:
            f.write("%s\n" % item)

    with open(f'audit_log_of_{fsg_id}.txt', 'r') as f:
        for line in f.readlines():
            line = line.replace(',', ',\n').replace('[', "").replace(']', "").replace("'", "")
        with open(f'audit_log_of_{fsg_id}.txt', 'w') as new_file:
            new_file.write(line)
    f.close()


def file_formatter(temp_text_file, desired_name):
    with open(f'{temp_text_file}.txt', 'r') as infile, \
            open(f'{desired_name}.txt', 'w') as outfile:
        data = infile.read()
        data = data.replace("[", "").replace("]", "").replace(")", "").replace("(", "").replace("'", "")
        outfile.write(data)
    os.remove(f"{temp_text_file}.txt")
    outfile.close()
    infile.close()


def set_file_header():
    file_header = ['FSG_ID', 'Product_ID', 'Client_ID', 'Quantity', 'Unit', 'Location']
    return file_header
