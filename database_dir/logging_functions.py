def get_locations_of_product_id(product_id, cursor):
    product_id = "'" + product_id + "'"
    result = cursor.execute(f'SELECT * FROM founders_inventory WHERE (product_id == {product_id}) '
                            f'AND quantity > 0;').fetchall()
    return result


def get_locations_of_product_id_historic(product_id, cursor):
    product_id = "'" + product_id + "'"
    result = cursor.execute(f'SELECT * FROM founders_inventory WHERE (product_id == {product_id});').fetchall()
    return result


def get_fsg_id_from_storage_location(storage_location, cursor):
    storage_location = "'" + storage_location + "'"
    result = cursor.execute(f'SELECT * FROM founders_inventory WHERE (storage_location == {storage_location}) '
                            f'AND quantity > 0;').fetchall()
    return result


def get_fsg_id_from_storage_location_historic(storage_location, cursor):
    storage_location = "'" + storage_location + "'"
    result = cursor.execute(f'SELECT * FROM founders_inventory WHERE (storage_location == {storage_location});')\
        .fetchall()
    return result


def get_fsg_id_by_client(client_id, cursor):
    client_id = "'" + client_id + "'"
    result = cursor.execute(f'SELECT * FROM founders_inventory WHERE (client_id == {client_id}) AND quantity > 0;')\
        .fetchall()
    return result


def get_fsg_id_by_client_historic(client_id, cursor):
    client_id = "'" + client_id + "'"
    result = cursor.execute(f'SELECT * FROM founders_inventory WHERE (client_id == {client_id});').fetchall()
    return result


def get_audit_log_by_fsg_id(fsg_id, cursor):
    fsg_id = "'" + fsg_id + "'"
    result = cursor.execute(f'SELECT fsg_id_event_log FROM founders_inventory WHERE (fsg_id == {fsg_id});').fetchall()
    return result
