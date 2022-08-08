import sqlite3


def duplicate_user_check(cursor: sqlite3.Cursor, username):
    username = "'" + username + "'"
    result = cursor.execute(f'SELECT username FROM user_table WHERE (username == {username});').fetchall()
    for row in result:
        result = row[0]
    username = username.replace("'", "")
    if result == username:
        return True
    return False


def user_exist(cursor: sqlite3.Cursor, username):
    username = "'" + username + "'"
    result = cursor.execute(f'SELECT username FROM user_table WHERE (username == {username});').fetchall()
    for row in result:
        result = row[0]
    username = username.replace("'", "")
    if result == username:
        return True
    return False


def get_user_initials(cursor: sqlite3.Cursor, username):
    username = "'" + username + "'"
    result = cursor.execute(f'SELECT initials FROM user_table WHERE (username == {username});').fetchall()
    for row in result:
        result = row[0]
    return result


def change_user_password(cursor: sqlite3.Cursor, connection, username, password, timestamp):
    username = "'" + username + "'"
    password = "'" + password + "'"
    cursor.execute(f'UPDATE user_table SET user_password = {password} AND timestamp = {timestamp} '
                   f'WHERE username = {username}')
    connection.commit()


def insert_into_user_table(cursor: sqlite3.Cursor, connection, entry_to_insert):
    cursor.executemany('''INSERT INTO user_table(username, user_password, initials, timestamp) VALUES(?, ?, ?, ?)''',
                       (entry_to_insert,))
    connection.commit()


def get_all_users(cursor):
    result = cursor.execute(f'SELECT * FROM user_table;').fetchall()
    list_of_locations = []
    counter = 0
    for row in result:
        list_of_locations.append(row[counter])
        counter = counter + 1

    return result
