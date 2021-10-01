import sqlite3

def con():
    try:
        sqlite_connection = sqlite3.connect('modules/sqlite/master_rune.db')
        return sqlite_connection
    except sqlite3.Error as error:
        print("error connect to sqlite", error)