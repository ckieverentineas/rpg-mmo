import datetime
from modules.sqlite.connect import con
from modules.sqlite.engine.select import be

def register(idvk):
    #создание персонажа
    check = be(idvk)
    if (check == False):
        #задание параметров
        lvl = 0
        attack = 0
        defmagic = 0
        defphysical = 0
        dexterity = 0
        intelligence = 0
        health = 0
        xp = 0
        gold = 0
        points = 5
        crdate = datetime.datetime.now()
        cursor = con()
        #Инициализация нового игрока
        sqlite_insert_with_param = """INSERT OR IGNORE INTO player
                                (idvk, lvl, attack, defmagic,
                                defphysical, dexterity, intelligence,
                                health, xp, gold, points, crdate)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        data_tuple = (idvk, lvl, attack, defmagic, defphysical,
                      dexterity, intelligence, health, xp, gold,
                      points, crdate)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        cursor.commit()
        cursor.close()
        return (f'Приветствую нового рунного мастера!')    
    return(f'Рунные мастера не сдаются.')

def generate_mob(idvk):
    #задание параметров
        lvl = 0
        attack = 0
        defmagic = 0
        defphysical = 0
        dexterity = 0
        intelligence = 0
        health = 0
        xp = 0
        gold = 0
        points = 5
        crdate = datetime.datetime.now()
        cursor = con()
        #Инициализация нового игрока
        sqlite_insert_with_param = """INSERT OR IGNORE INTO mob
                                (idvk, lvl, attack, defmagic,
                                defphysical, dexterity, intelligence,
                                health, xp, gold, points, crdate)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        data_tuple = (idvk, lvl, attack, defmagic, defphysical,
                      dexterity, intelligence, health, xp, gold,
                      points, crdate)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        cursor.commit()
        cursor.close()