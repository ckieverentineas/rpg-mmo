import datetime
from random import randint, random
from modules.sqlite.connect import con
from modules.sqlite.engine.select import be, select

def register(idvk):
    #создание персонажа
    check = be(idvk)
    if (check == False):
        #задание параметров
        lvl = 0
        attack = 0
        defence = 0
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
                                (idvk, lvl, attack, defence,
                                dexterity, intelligence,
                                health, xp, gold, points, crdate)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        data_tuple = (idvk, lvl, attack, defence,
                      dexterity, intelligence, health, xp, gold,
                      points, crdate)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        cursor.commit()
        cursor.close()
        return (f'Приветствую нового рунного мастера!')    
    return(f'Рунные мастера не сдаются.')


def generate_mob(idvk):
    #задание параметров
    source = select('player', 'lvl', idvk)
    lvl = int(source[0]["lvl"])
    attack = 0
    defence = 0
    dexterity = 0
    intelligence = 0
    health = 0
    xp = 1 + lvl + randint(0,lvl)*random()
    gold = 1 + lvl + randint(0,lvl)*random()
    points = 5+lvl*2*lvl
    crdate = datetime.datetime.now()
    while (points > 0):
        if(points > 0):
            attack = attack + 1
            points = points - 1
        if(points > 0):
            defence = defence + 1
            points = points - 1
        if(points > 0):
            dexterity = dexterity + 1
            points = points - 1
        if(points > 0):
            intelligence = intelligence + 1
            points = points - 1
        if(points > 0):
            health = health + 2
            points = points - 1
    attack = attack + randint(0,lvl)*random()
    defence = defence + randint(0,lvl)*random()
    dexterity = dexterity + randint(0,lvl)*random()
    intelligence = intelligence + randint(0,lvl)*random()
    health = health + randint(0,lvl)*random()
    cursor = con()
    #Инициализация нового игрока
    sqlite_insert_with_param = """INSERT OR IGNORE INTO mob
                                (idvk, lvl, attack, defence,
                                dexterity, intelligence,
                                health, xp, gold, points, crdate)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    data_tuple = (idvk, lvl, attack, defence,
                  dexterity, intelligence, health, int(xp), int(gold),
                  points, crdate)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    cursor.commit()
    cursor.close()
    print(f'Mob was generated')

def generate_battle(idvk):
    #инициализация битвы
    mob = select('mob', 'lvl, xp, gold, points, attack, defence, dexterity, intelligence, health', idvk)
    player = select('player', 'lvl, xp, gold, points, attack, defence, dexterity, intelligence, health', idvk)
    crdate = datetime.datetime.now()
    cursor = con()
    #подготовка к битве
    sqlite_insert_with_param = """INSERT OR IGNORE INTO battlepve
                                (idvk, attackplayer, defenceplayer, dexterityplayer,
                                 intelligenceplayer, healthplayer, manaplayer,
                                 attackmob, defencemob, dexteritymob,
                                 intelligencemob, healthmob, manamob, crdate)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    data_tuple = (idvk, player[0]["attack"], player[0]["defence"],
                  player[0]["dexterity"], player[0]["intelligence"],
                  player[0]["health"], player[0]["intelligence"],
                  mob[0]["attack"], mob[0]["defence"],
                  mob[0]["dexterity"], mob[0]["intelligence"],
                  mob[0]["health"], mob[0]["intelligence"], crdate)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    cursor.commit()
    cursor.close()
    print(f'Mob and Player added in Temp for {idvk}')