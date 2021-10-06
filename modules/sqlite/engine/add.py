import datetime
from os import stat
import random
from modules.sqlite.connect import con
from modules.sqlite.engine.select import battle_dexterity_equal, be, select

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
        status += generate_inventory_for_player(idvk)
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
    itemid = 0
    crdate = datetime.datetime.now()
    cursor = con()
    #Инициализация нового игрока
    sqlite_insert_with_param = """INSERT OR IGNORE INTO setting
                                (idvk, lvl, costattack, itemid, crdate)
                                VALUES (?, ?, ?, ?, ?);"""
    data_tuple = (idvk, lvl, costattack, itemid, crdate)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    cursor.commit()
    cursor.close()
    print(f'Settings init for player: {idvk}')
    status = f'\n\n Параметры персонажа инициализированы \n\n'
    return status  

def generate_inventory_for_player(idvk):
    #создание инвентаря пользователя
    mythical = 0
    legendary = 0
    epic = 0
    rare = 0
    unusual = 0
    usual = 0
    water = 0
    runic = 0
    flower = 0
    potionlife = 0
    potionmana = 0
    crdate = datetime.datetime.now()
    cursor = con()
    #Инициализация инвентаря нового игрока
    sqlite_insert_with_param = """INSERT OR IGNORE INTO inventory
                                (idvk, mythical, legendary, epic, rare, unusual, usual, water, runic, flower, potionlife, potionmana, crdate)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    data_tuple = (idvk, mythical, legendary, epic, rare, unusual, usual, water, runic, flower, potionlife, potionmana, crdate)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    cursor.commit()
    cursor.close()
    print(f'Inventory init for player: {idvk}')
    status = f'\n\n Инвентарь персонажа инициализирован \n\n'
    return status 

def generate_reward_for_player(idvk):
    #создание настроек персонажа
    xp = 7000
    gold = 584
    crdate = datetime.datetime.now()
    cursor = con()
    #Инициализация нового игрока
    sqlite_insert_with_param = """INSERT OR IGNORE INTO reward
                                (idvk, xp, gold, crdate)
                                VALUES (?, ?, ?, ?);"""
    data_tuple = (idvk, xp, gold, crdate)
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
    points = 0
    status = f'\n\nВы получили руну:\n'
    ranger = random.SystemRandom(lvl).randint(1, 10000)
    if (ranger == 1):
        points = 6
        status += f'\nРуна оказалась мифической\n'
    if (ranger >= 2 and ranger <= 5):
        points = 5
        status += f'\nРуна оказалась легендарной\n'
    if (ranger >= 6 and ranger <= 20):
        points = 4
        status += f'\nРуна оказалась эпической\n'
    if (ranger >= 21 and ranger <= 65):
        points = 3
        status += f'\nРуна оказалась редкой\n'
    if (ranger >= 66 and ranger <= 200):
        points = 2
        status += f'\nРуна оказалась необычной\n'
    if (ranger >= 201 and ranger <= 500):
        points = 1
        status += f'\nРуна оказалась обычной\n'
    if (points == 0):
        print(f'Rune destroy on generate part for player {idvk}')
        return False
    while (points > 0):
        stat = random.SystemRandom(lvl).randint(1, 6)
        if (stat == 1 and attack == 0):
            attack = random.SystemRandom(lvl).randint(-lvl, lvl)
            if (attack != 0):
                points = points - 1
        if (stat == 2 and defence == 0):
            defence = random.SystemRandom(lvl).randint(-lvl, lvl)
            if (defence != 0):
                points = points - 1
        if (stat == 3 and defencemagic == 0):
            defencemagic = random.SystemRandom(lvl).randint(-lvl, lvl)
            if (defencemagic != 0):
                points = points - 1
        if (stat == 4 and dexterity == 0):
            dexterity = random.SystemRandom(lvl).randint(-lvl, lvl)
            if (dexterity != 0):
                points = points - 1
        if (stat == 5 and intelligence == 0):
            intelligence = random.SystemRandom(lvl).randint(-lvl, lvl)
            if (intelligence != 0):
                points = points - 1
        if (stat == 6 and health == 0):
            health = random.SystemRandom(lvl).randint(-lvl, lvl)
            if (health != 0):
                points = points - 1
        """
        if (stat == 6 and xp == 0):
            xp = random.SystemRandom(lvl).randint(-lvl, lvl) + random.SystemRandom(lvl).randint(0, lvl)*random.SystemRandom(lvl).uniform(-0.30, 0.30)
            points = points - 1
        if (stat == 7 and gold  == 0):
            gold = random.SystemRandom(lvl).randint(-lvl, lvl) + random.SystemRandom(lvl).randint(0, lvl)*random.SystemRandom(lvl).uniform(-0.30, 0.30)
            points = points - 1
        if (stat == 8 and loot == 0):
            loot = random.SystemRandom(lvl).randint(-lvl, lvl) + random.SystemRandom(lvl).randint(0, lvl)*random.SystemRandom(lvl).uniform(-0.30, 0.30)
            points = points - 1"""
    
    cursor = con()
    #Инициализация новой руны
    sqlite_insert_with_param = """INSERT OR IGNORE INTO rune
                                (idvk, lvl, attack, defence, defencemagic,
                                dexterity, intelligence,
                                health, xp, gold, loot, equip, crdate)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    data_tuple = (idvk, lvl, int(attack), int(defence), int(defencemagic),
                      int(dexterity), int(intelligence), int(health), int(xp), int(gold),
                      int(loot), equip, crdate)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    cursor.commit()
    cursor.close()
    print(f'Founding new rune for player {idvk}')
    return status

def creator(idvk):
    #воссоздание руны
    player = select('mob', 'lvl', idvk)
    lvl = player[0]["lvl"]
    inventory = select('inventory', 'mythical, legendary, epic, rare, unusual, usual', idvk)
    mythical = inventory[0]["mythical"]
    legendary = inventory[0]["legendary"]
    epic = inventory[0]["epic"]
    rare = inventory[0]["rare"]
    unusual = inventory[0]["unusual"]
    usual = inventory[0]["usual"]
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
    points = 0
    status = f'\n\nВы воссоздали руну:\n'
    if (mythical >= 10):
        target = f'mythical'
        points = 6
        statusr = f'\nРуна оказалась мифической\n'
    if (legendary >= 10):
        target = f'legendary'
        points = 5
        statusr = f'\nРуна оказалась легендарной\n'
    if (epic >= 10):
        target = f'epic'
        points = 4
        statusr = f'\nРуна оказалась эпической\n'
    if (rare >= 10):
        target = f'rare'
        points = 3
        statusr = f'\nРуна оказалась редкой\n'
    if (unusual >= 10):
        target = f'unusual'
        points = 2
        statusr = f'\nРуна оказалась необычной\n'
    if (usual >= 0):
        target = f'usual'
        points = 1
        statusr = f'\nРуна оказалась обычной\n'
    if (points == 0):
        status = f'\nНедостаточно обломков для создания руны\n'
        print(f'Rune can not create for player {idvk}')
        return status
    status += statusr
    use = select('inventory', target, idvk)
    update('inventory', target, use[0][target]-10, idvk)
    while (points > 0):
        stat = random.SystemRandom(lvl).randint(1, 6)
        if (stat == 1 and attack == 0):
            attack = random.SystemRandom(lvl).randint(-lvl, lvl)
            if (attack != 0):
                points = points - 1
        if (stat == 2 and defence == 0):
            defence = random.SystemRandom(lvl).randint(-lvl, lvl)
            if (defence != 0):
                points = points - 1
        if (stat == 3 and defencemagic == 0):
            defencemagic = random.SystemRandom(lvl).randint(-lvl, lvl)
            if (defencemagic != 0):
                points = points - 1
        if (stat == 4 and dexterity == 0):
            dexterity = random.SystemRandom(lvl).randint(-lvl, lvl)
            if (dexterity != 0):
                points = points - 1
        if (stat == 5 and intelligence == 0):
            intelligence = random.SystemRandom(lvl).randint(-lvl, lvl)
            if (intelligence != 0):
                points = points - 1
        if (stat == 6 and health == 0):
            health = random.SystemRandom(lvl).randint(-lvl, lvl)
            if (health != 0):
                points = points - 1
        """
        if (stat == 6 and xp == 0):
            xp = random.SystemRandom(lvl).randint(-lvl, lvl) + random.SystemRandom(lvl).randint(0, lvl)*random.SystemRandom(lvl).uniform(-0.30, 0.30)
            points = points - 1
        if (stat == 7 and gold  == 0):
            gold = random.SystemRandom(lvl).randint(-lvl, lvl) + random.SystemRandom(lvl).randint(0, lvl)*random.SystemRandom(lvl).uniform(-0.30, 0.30)
            points = points - 1
        if (stat == 8 and loot == 0):
            loot = random.SystemRandom(lvl).randint(-lvl, lvl) + random.SystemRandom(lvl).randint(0, lvl)*random.SystemRandom(lvl).uniform(-0.30, 0.30)
            points = points - 1"""
    
    cursor = con()
    #Инициализация новой руны
    sqlite_insert_with_param = """INSERT OR IGNORE INTO rune
                                (idvk, lvl, attack, defence, defencemagic,
                                dexterity, intelligence,
                                health, xp, gold, loot, equip, crdate)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    data_tuple = (idvk, lvl, int(attack), int(defence), int(defencemagic),
                      int(dexterity), int(intelligence), int(health), int(xp), int(gold),
                      int(loot), equip, crdate)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    cursor.commit()
    cursor.close()
    status += print_rune_last_gen(idvk)
    print(f'Created new rune for player {idvk}')
    return status


def update(table, row, data, idvk):
    cursor = con()
    sql_update_query = (f'UPDATE {table} SET {row} = ? WHERE idvk = ?;')
    data_tuple = (data, idvk)
    cursor.execute(sql_update_query, data_tuple)
    cursor.commit()
    cursor.commit()
    cursor.close()

def update_item(table, row, data, idvk, itemid):
    cursor = con()
    sql_update_query = (f'UPDATE {table} SET {row} = ? WHERE idvk = ? and id = ?;')
    data_tuple = (data, idvk, itemid)
    cursor.execute(sql_update_query, data_tuple)
    cursor.commit()
    cursor.commit()
    cursor.close()

def delete(table, idvk):
    #Функция удаления данных
    cursor = con()
    sql_delete_query = (f'DELETE from {table} WHERE idvk = {idvk}')
    cursor.execute(sql_delete_query)
    cursor.commit()
    print(f'Deleted record {table} for {idvk}')
    cursor.close()

def delete_item(table, idvk, itemid):
    cursor = con()
    sql_delete_query = (f'DELETE from {table} WHERE idvk = {idvk} and id = {itemid}')
    cursor.execute(sql_delete_query)
    cursor.commit()
    print(f'Deleted item {table} {itemid} for {idvk}')
    cursor.close()

def select(table, row, idvk):
    cursor = con()
    cursor.row_factory = sqlite3.Row
    line = cursor.execute(f'SELECT {row} FROM {table} WHERE idvk = {idvk}')
    rows  = line.fetchall()
    return rows
    
def select_item(table, row, idvk, itemid):
    cursor = con()
    cursor.row_factory = sqlite3.Row
    line = cursor.execute(f'SELECT {row} FROM {table} WHERE idvk = {idvk} and id = {itemid}')
    rows  = line.fetchall()
    return rows

def select_equip(table, row, idvk):
    cursor = con()
    cursor.row_factory = sqlite3.Row
    line = cursor.execute(f'SELECT {row} FROM {table} WHERE idvk = {idvk} and equip = "yes"')
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

def reseach(idvk):
    delete('mob_current',idvk)
    delete('player_current',idvk)
    delete('mob',idvk)
    generate_mob(idvk)
    generate_battle(idvk)
    costattack = battle_dexterity_equal(idvk)
    update('setting', 'costattack', costattack, idvk)
    use_runes_equip(idvk)
    status = print_mob_profile(idvk)
    return status