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
        defencemagic = 0
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
                                (idvk, lvl, attack, defence, defencemagic,
                                dexterity, intelligence,
                                health, xp, gold, points, crdate)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        data_tuple = (idvk, lvl, attack, defence, defencemagic,
                      dexterity, intelligence, health, xp, gold,
                      points, crdate)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        cursor.commit()
        cursor.close()
        print(f'Register new master: {idvk}.')
        return (f'Приветствую нового рунного мастера!')   
    print(f'Master not forrgot skills {idvk}.') 
    return(f'Рунные мастера не сдаются.')


def generate_mob(idvk):
    #задание параметров
    source = select('player', 'lvl', idvk)
    lvl = int(source[0]["lvl"])
    attack = 0
    defence = 0
    defencemagic = 0
    dexterity = 0
    intelligence = 0
    health = 0
    xp = 1 + randint(0,lvl) + randint(0,lvl)*random()
    gold = 1 + randint(0,lvl) + randint(0,lvl)*random()
    points = 5+lvl*2*lvl
    crdate = datetime.datetime.now()
    while (points > 0):
        if(points > 0):
            attack = attack + 2
            points = points - 1
        if(points > 0):
            defence = defence + 3
            points = points - 1
        if(points > 0):
            health = health + 4
            points = points - 1
        if(points > 0):
            dexterity = dexterity + 2
            points = points - 1
        if(points > 0):
            intelligence = intelligence + 2
            points = points - 1
        if(points > 0):
            defencemagic = defencemagic + 3
            points = points - 1
    attack = attack + randint(0,lvl)*random()
    defence = defence + randint(0,lvl)*random()
    defencemagic = defencemagic + randint(0,lvl)*random()
    dexterity = dexterity + randint(0,lvl)*random()
    intelligence = intelligence + randint(0,lvl)*random()
    health = health + randint(0,lvl)*random()
    cursor = con()
    #Инициализация нового игрока
    sqlite_insert_with_param = """INSERT OR IGNORE INTO mob
                                (idvk, lvl, attack, defence, defencemagic,
                                dexterity, intelligence,
                                health, xp, gold, points, crdate)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    data_tuple = (idvk, lvl, attack, defence, defencemagic,
                  dexterity, intelligence, health, int(xp), int(gold),
                  points, crdate)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    cursor.commit()
    cursor.close()
    print(f'Mob was generated for {idvk}')

def generate_battle(idvk):
    #инициализация битвы
    mob = select('mob', 'attack, defence, defencemagic, dexterity, intelligence, health', idvk)
    player = select('player', 'attack, defence, defencemagic, dexterity, intelligence, health', idvk)
    crdate = datetime.datetime.now()
    cursor = con()
    #подготовка к битве игрока
    sqlite_insert_with_param = """INSERT OR IGNORE INTO player_current
                                (idvk, attack, defence, defencemagic, dexterity, intelligence, health, mana, crdate)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    data_tuple = (idvk, player[0]["attack"], player[0]["defence"], player[0]["defencemagic"],
                  player[0]["dexterity"], player[0]["intelligence"],
                  player[0]["health"], player[0]["intelligence"]*2, crdate)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    cursor.commit()
    #подготовка к битве моба
    sqlite_insert_with_param = """INSERT OR IGNORE INTO mob_current
                                (idvk, attack, defence, defencemagic, dexterity, intelligence, health, mana, crdate)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    data_tuple = (idvk, mob[0]["attack"], mob[0]["defence"], mob[0]["defencemagic"],
                  mob[0]["dexterity"], mob[0]["intelligence"],
                  mob[0]["health"], mob[0]["intelligence"]*2, crdate)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    cursor.commit()
    cursor.close()
    print(f'Generate PVE event for {idvk}')