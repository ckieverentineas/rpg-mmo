import datetime
from os import stat
import random
from modules.sqlite.connect import con
from modules.sqlite.engine.select import battle_dexterity_equal, be, select
from modules.sqlite.engine.update import *

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
        status = f'\n\n Приветствую нового рунного мастера! \n\n'
        status += generate_setting_for_player(idvk)
        status += generate_reward_for_player(idvk)
        return status  
    print(f'Master not forrgot skills {idvk}.') 
    status = f'Рунные мастера не сдаются'
    return status


def generate_mob(idvk):
    #задание параметров
    source = select('setting', 'lvl', idvk)
    lvl = int(source[0]["lvl"])
    attack = 0
    defence = 0
    defencemagic = 0
    dexterity = 0
    intelligence = 0
    health = 0
    xp = 1 + lvl+lvl*random.SystemRandom(lvl).uniform(-0.30, 0.30)
    gold = 1 + lvl+lvl*random.SystemRandom(lvl).uniform(-0.30, 0.30)
    points = 5+2*lvl
    crdate = datetime.datetime.now()
    while (points > 0):
        if(points > 0):
            health = health + 4
            points = points - 1
        if(points > 0):
            defence = defence + 3
            points = points - 1
        if(points > 0):
            attack = attack + 2
            points = points - 1
        if(points > 0):
            dexterity = dexterity + 2
            points = points - 1
        if(points > 0):
            intelligence = intelligence + 2
            points = points - 1
        if(points > 0):
            defence = defence + 3
            points = points - 1
        
        if(points > 0):
            defencemagic = defencemagic + 3
            points = points - 1
        if(points > 0):
            health = health + 4
            points = points - 1
        if(points > 0):
            dexterity = dexterity + 2
            points = points - 1
        if(points > 0):
            attack = attack + 2
            points = points - 1
        if(points > 0):
            defence = defence + 3
            points = points - 1
        if(points > 0):
            intelligence = intelligence + 2
            points = points - 1
        
        if(points > 0):
            health = health + 4
            points = points - 1
        if(points > 0):
            defence = defence + 3
            points = points - 1
        if(points > 0):
            dexterity = dexterity + 2
            points = points - 1
        if(points > 0):
            attack = attack + 2
            points = points - 1
        if(points > 0):
            defencemagic = defencemagic + 3
            points = points - 1
        if(points > 0):
            defence = defence + 3
            points = points - 1
        if(points > 0):
            dexterity = dexterity + 2
            points = points - 1
        if(points > 0):
            intelligence = intelligence + 2
            points = points - 1
    attack = attack + attack*random.SystemRandom(attack).uniform(-0.30, 0.30)
    defence = defence + defence*random.SystemRandom(defence).uniform(-0.30, 0.30) 
    defencemagic = defencemagic + defencemagic*random.SystemRandom(defencemagic).uniform(-0.30, 0.30)
    dexterity = dexterity + dexterity*random.SystemRandom(dexterity).uniform(-0.30, 0.30)
    intelligence = intelligence + intelligence*random.SystemRandom(intelligence).uniform(-0.30, 0.30)
    health = health + health*random.SystemRandom(health).uniform(-0.30, 0.30)
    cursor = con()
    #Инициализация нового игрока
    sqlite_insert_with_param = """INSERT OR IGNORE INTO mob
                                (idvk, lvl, attack, defence, defencemagic,
                                dexterity, intelligence,
                                health, xp, gold, points, crdate)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    data_tuple = (idvk, lvl, int(attack), int(defence), int(defencemagic),
                  int(dexterity), int(intelligence), int(health), int(xp), int(gold),
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

def generate_setting_for_player(idvk):
    #создание настроек персонажа
    lvl = 0
    costattack = 0
    crdate = datetime.datetime.now()
    cursor = con()
    #Инициализация нового игрока
    sqlite_insert_with_param = """INSERT OR IGNORE INTO setting
                                (idvk, lvl, costattack, crdate)
                                VALUES (?, ?, ?, ?);"""
    data_tuple = (idvk, lvl, costattack, crdate)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    cursor.commit()
    cursor.close()
    print(f'Settings init for player: {idvk}')
    status = f'\n\n Параметры персонажа инициализированы \n\n'
    return status  

def generate_reward_for_player(idvk):
    #создание настроек персонажа
    xp = 5000
    crdate = datetime.datetime.now()
    cursor = con()
    #Инициализация нового игрока
    sqlite_insert_with_param = """INSERT OR IGNORE INTO reward
                                (idvk, xp, crdate)
                                VALUES (?, ?, ?);"""
    data_tuple = (idvk, xp, crdate)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    cursor.commit()
    cursor.close()
    print(f'Rewards init for player: {idvk}')
    status = f'\n\n Награды добавлены. Дла их получения напишите: wipe\n\n'
    return status  

def generate_rune(idvk):
    #создание руны
    player = select('mob', 'lvl', idvk)
    lvl = player[0]["lvl"]
    attack = 0
    defence = 0
    defencemagic = 0
    dexterity = 0
    intelligence = 0
    health = 0
    xp = 0
    gold = 0
    loot = 0
    equip = "no"
    crdate = datetime.datetime.now()
    points = 1
    ranger = random.SystemRandom(lvl).randint(0, 10000)
    if (ranger < 100):
        points = 2
    if (ranger < 30):
        points = 3
    if (ranger < 14):
        points = 4
    if (ranger < 5):
        points = 5
    if (ranger < 1):
        points = 6
    while (points > 0):
        stat = random.SystemRandom(lvl).randint(0, 9)
        if (stat == 0 and attack == 0):
            attack = random.SystemRandom(lvl).randint(-lvl, lvl) + random.SystemRandom(lvl).randint(0, lvl)*random.SystemRandom(lvl).uniform(-0.30, 0.30)
            points = points - 1
        if (stat == 1 and defence == 0):
            defence = random.SystemRandom(lvl).randint(-lvl, lvl) + random.SystemRandom(lvl).randint(0, lvl)*random.SystemRandom(lvl).uniform(-0.30, 0.30)
            points = points - 1
        if (stat == 2 and defencemagic == 0):
            defencemagic = random.SystemRandom(lvl).randint(-lvl, lvl) + random.SystemRandom(lvl).randint(0, lvl)*random.SystemRandom(lvl).uniform(-0.30, 0.30)
            points = points - 1
        if (stat == 3 and dexterity == 0):
            dexterity = random.SystemRandom(lvl).randint(-lvl, lvl) + random.SystemRandom(lvl).randint(0, lvl)*random.SystemRandom(lvl).uniform(-0.30, 0.30)
            points = points - 1
        if (stat == 4 and intelligence == 0):
            intelligence = random.SystemRandom(lvl).randint(-lvl, lvl) + random.SystemRandom(lvl).randint(0, lvl)*random.SystemRandom(lvl).uniform(-0.30, 0.30)
            points = points - 1
        if (stat == 5 and health == 0):
            health = random.SystemRandom(lvl).randint(-lvl, lvl) + random.SystemRandom(lvl).randint(0, lvl)*random.SystemRandom(lvl).uniform(-0.30, 0.30)
            points = points - 1
        if (stat == 6 and xp == 0):
            xp = random.SystemRandom(lvl).randint(-lvl, lvl) + random.SystemRandom(lvl).randint(0, lvl)*random.SystemRandom(lvl).uniform(-0.30, 0.30)
            points = points - 1
        if (stat == 7 and gold  == 0):
            gold = random.SystemRandom(lvl).randint(-lvl, lvl) + random.SystemRandom(lvl).randint(0, lvl)*random.SystemRandom(lvl).uniform(-0.30, 0.30)
            points = points - 1
        if (stat == 8 and loot == 0):
            loot = random.SystemRandom(lvl).randint(-lvl, lvl) + random.SystemRandom(lvl).randint(0, lvl)*random.SystemRandom(lvl).uniform(-0.30, 0.30)
            points = points - 1
    
    cursor = con()
    #Инициализация новой руны
    sqlite_insert_with_param = """INSERT OR IGNORE INTO rune
                                (idvk, attack, defence, defencemagic,
                                dexterity, intelligence,
                                health, xp, gold, loot, equip, crdate)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    data_tuple = (idvk, int(attack), int(defence), int(defencemagic),
                      int(dexterity), int(intelligence), int(health), int(xp), int(gold),
                      int(loot), equip, crdate)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    cursor.commit()
    cursor.close()
    print(f'Founding new rune for player {idvk}')