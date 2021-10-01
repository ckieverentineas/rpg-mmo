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
        #ход игрока
        
        print(f'Ходит игрок')
        #проверка на готовность доп хода игроком
        #атака по мобу
    else:
        #ход врага
        #проверка на доп ходы мобом их активация
        print(f'Ходит враг')