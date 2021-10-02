import sqlite3
from modules.sqlite.connect import con
#запросы к базам данных
def select(table, row, idvk):
    cursor = con()
    cursor.row_factory = sqlite3.Row
    line = cursor.execute(f'SELECT {row} FROM {table} WHERE idvk = {idvk}')
    rows  = line.fetchall()
    return rows
    
def be(idvk):
    #проверка на наличие аккаунта
    info = select('player', 'id', idvk)
    if (not info):
        return False
    return True

def battle_dexterity_equal(idvk):
    player = select('player', 'dexterity', idvk)
    mob = select('mob', 'dexterity', idvk)
    if (player[0]["dexterity"] > mob[0]["dexterity"]):
        return mob[0]["dexterity"]
    else:
        return player[0]["dexterity"]