from modules.sqlite.connect import con
from modules.sqlite.createtable import createdb

def crdb():
    try:
        cursor = con()
        createdb()
        cursor.close()
    except:
        print("db get error")
crdb()
