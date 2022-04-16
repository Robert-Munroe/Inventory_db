import database
import entrybuilder


def get_entry(db_cursor, connection):
    entry = entrybuilder.build_entry()
    database.insert_into_inventory_table(db_cursor, connection, entry)
    print(entry)


def main():
    connection, db_cursor = database.open_db("foundersinventorydb.sqlite")
    database.create_table(db_cursor)
    prompt = "Please press 1 to enter a new entry\n" \
             "Please press 2 to view a sample's info\n" \
             "Press 3 to close the program\n"
    runner = 0

    while runner != -1:
        runner = int(input(prompt))
        if runner == 1:
            get_entry(db_cursor, connection)
        if runner == 2:
            database.get_product_info(db_cursor, connection)
        if runner == 3:
            runner = -1


if __name__ == '__main__':
    main()

