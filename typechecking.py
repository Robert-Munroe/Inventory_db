import re
import database


def is_product_date_formatted_correctly(date):
    if type(date) == str:
        match = re.match("[0-9][0-9][/][0-9][0-9][/][0-9][0-9][0-9][0-9]", date)
        is_match = bool(match)
        if is_match:
            if len(date) == 10:
                return 0
            else:
                return 1
        else:
            return 1
    else:
        return 1


def is_product_id_formatted_correctly(product_id):
    connection, db_cursor = database.open_db("foundersinventorydb.sqlite")
    if type(product_id) == str:
        match = re.match("[0-9][0-9][S,R][0-9][0-9][0-9][0-9]", product_id)
        is_match = bool(match)
        if is_match:
            if len(product_id) == 7:
                if database.get_product_id_from_db(db_cursor, product_id) == 0:
                    return 0
                else:
                    print("This product ID already exists")
                    return 1
            else:
                print("incorrectly formatted")
                return 1
        else:
            print("product entered incorrectly")
            return 1
    else:
        print("product entered incorrectly")
        return 1
