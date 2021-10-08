import datetime
from os import stat
import random
import sqlite3
from modules.sqlite.connect import con


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
    lvlmobkilled = 0
    crdate = datetime.datetime.now()
    cursor = con()
    #Инициализация нового игрока
    sqlite_insert_with_param = """INSERT OR IGNORE INTO setting
                                (idvk, lvl, costattack, itemid, lvlmobkilled, crdate)
                                VALUES (?, ?, ?, ?, ?, ?);"""
    data_tuple = (idvk, lvl, costattack, itemid, lvlmobkilled, crdate)
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
    lvl = 18
    points = 18
    gold = 3655
    mythical = 0
    legendary = 0
    epic = 30
    rare = 10
    unusual = 70
    usual = 110
    crdate = datetime.datetime.now()
    cursor = con()
    #Инициализация нового игрока
    sqlite_insert_with_param = """INSERT OR IGNORE INTO reward
                                (idvk, lvl, gold, points, mythical, legendary, epic, rare, unusual, usual, crdate)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    data_tuple = (idvk, lvl, gold, points, mythical, legendary, epic, rare, unusual, usual, crdate)
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
    try:
        player = select('setting', 'lvlmobkilled', idvk)
        lvl = player[0]["lvlmobkilled"]
        inventory = select('inventory', 'legendary, epic, rare, unusual, usual', idvk)
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
        if (legendary >= 10):
            target = f'legendary'
            points = 6
            statusr = f'\nВы создали мифическую руну\n'
        if (epic >= 10):
            target = f'epic'
            points = 5
            statusr = f'\nВы создали легендарную руну\n'
        if (rare >= 10):
            target = f'rare'
            points = 4
            statusr = f'\nВы создали эпическую руну\n'
        if (unusual >= 10):
            target = f'unusual'
            points = 3
            statusr = f'\nВы создали редкую руну\n'
        if (usual >= 0):
            target = f'usual'
            points = 2
            statusr = f'\nВы создали необычную руну\n'
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
        status += rune_down(idvk)
        print(f'Created new rune for player {idvk}')
        return status
    except:
        return f'Недостаточный уровень максимально убитого моба для создания рун!'

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

def set_player_attack(idvk):
    #добавление атаки
    source = select('player','attack, points', idvk)
    point = source[0]["points"]
    if (point > 0):
        stats = source[0]["attack"]
        stat = stats + 2
        update('player','attack', stat, idvk)
        point = point - 1
        update('player','points', point, idvk)
        print(f'Attack was {stats}, now {stat} for {idvk}.')
        status = f'Ваша атака возросла с {stats} до {stat} \n Очков осталось {point}'
        return status
    print(f'Have not points more for {idvk}.')
    status = f'У вас {point} очков. Повышение невозможно.'
    return status

def set_player_defence(idvk):
    #добавление магической защиты
    source = select('player','defence, points', idvk)
    point = source[0]["points"]
    if (point > 0):
        stats = source[0]["defence"]
        stat = stats + 3
        update('player','defence', stat, idvk)
        point = point - 1
        update('player','points', point, idvk)
        print(f'Defence was {stats}, now {stat} for {idvk}.')
        status = f'Ваша физическая защита возросла с {stats} до {stat} \n Очков осталось {point}'
        return status
    print(f'Have not points more for {idvk}.')
    status = f'У вас {point} очков. Повышение невозможно.'
    return status

def set_player_defencemagic(idvk):
    #добавление магической защиты
    source = select('player','defencemagic, points', idvk)
    point = source[0]["points"]
    if (point > 0):
        stats = source[0]["defencemagic"]
        stat = stats + 3
        update('player','defencemagic', stat, idvk)
        point = point - 1
        update('player','points', point, idvk)
        print(f'Defencemagic was {stats}, now {stat} for {idvk}.')
        status = f'Ваша магическая защита возросла с {stats} до {stat} \n Очков осталось {point}'
        return status
    print(f'Have not points more for {idvk}.')
    status = f'У вас {point} очков. Повышение невозможно.'
    return status

def set_player_dexterity(idvk):
    #добавление атаки
    source = select('player','dexterity, points', idvk)
    point = source[0]["points"]
    if (point > 0):
        stats = source[0]["dexterity"]
        stat = stats + 2
        update('player','dexterity', stat, idvk)
        point = point - 1
        update('player','points', point, idvk)
        print(f'Dexterity was {stats}, now {stat} for {idvk}.')
        status = f'Ваша ловкость возросла с {stats} до {stat} \n Очков осталось {point}'
        return status
    print(f'Have not points more for {idvk}.')
    status = f'У вас {point} очков. Повышение невозможно.'
    return status

def set_player_intelligence(idvk):
    #добавление атаки
    source = select('player','intelligence, points', idvk)
    point = source[0]["points"]
    if (point > 0):
        stats = source[0]["intelligence"]
        stat = stats + 2
        update('player','intelligence', stat, idvk)
        point = point - 1
        update('player','points', point, idvk)
        print(f'Intelligence was {stats}, now {stat} for {idvk}.')
        status = f'Ваш интеллект возрос с {stats} до {stat} \n Очков осталось {point}'
        return status
    print(f'Have not points more for {idvk}.')
    status = f'У вас {point} очков. Повышение невозможно.'
    return status

def set_player_health(idvk):
    #добавление атаки
    source = select('player','health, points', idvk)
    point = source[0]["points"]
    if (point > 0):
        stats = source[0]["health"]
        stat = stats + 4
        update('player','health', stat, idvk)
        point = point - 1
        update('player','points', point, idvk)
        print(f'Health was {stats}, now {stat} for {idvk}.')
        status = f'Ваше здоровье возросло с {stats} до {stat} \n Очков осталось {point}'
        return status
    print(f'Have not points more for {idvk}.')
    status = f'У вас {point} очков. Повышение невозможно.'
    return status

def clear_player_points(idvk):
    def gen_status(text, enter):
        if (enter > 0):
            status = f'Сброшен параметр {text} на {enter} очков. \n'
            return status
        status = f'В параметре {text} сбрасывать нечего. \n'
        return status

    #сброс параметров персонажа
    source = select('player','attack, defence, defencemagic, dexterity, intelligence, health, points', idvk)
    point = 0
    points = source[0]["points"]
    status = ""
    #обнуляем атаку
    stat = source[0]["attack"]
    point = point + stat/2
    update('player','attack', 0, idvk)
    status += gen_status('Атака', stat/2)
    # обнуляем физическую защиту
    stat = source[0]["defence"]
    point = point + stat/3
    update('player','defence', 0, idvk)
    status += gen_status('Физическая защита', stat/3)
    # обнуляем защиту
    stat = source[0]["defencemagic"]
    point = point + stat/3
    update('player','defencemagic', 0, idvk)
    status += gen_status('Магическая защита', stat/3)
    #обнуляем ловкость
    stat = source[0]["dexterity"]
    point = point + stat/2
    update('player','dexterity', 0, idvk)
    status += gen_status('Ловкость', stat/2)
    #обнуляем интеллект
    stat = source[0]["intelligence"]
    point = point + stat/2
    update('player','intelligence', 0, idvk)
    status += gen_status('Интеллект', stat/2)
    #обнуляем здоровье
    stat = source[0]["health"]
    if (stat > 0):
        point = point + stat/4
    update('player','health', 0, idvk)
    status += gen_status('Здоровье', stat/4)
    #начисляем очки
    points = points + int(point)
    update('player', 'points', points, idvk)
    status += f'🌟Начислено {int(point)} очков параметров.'
    print(f'Return {int(point)} for rebalance avatar by {idvk}.')
    return status

def player_attack_defence(idvk):
    #атака игрока
    player = select('player_current', 'attack', idvk)
    mob = select('mob_current','health, defence', idvk)
    damage = player[0]["attack"] - mob[0]["defence"]
    status = ""
    result = 0
    if (damage > 0):
        health = mob[0]["health"] - damage
        result = damage
        status += f'\n\n⚔Вы нанесли {damage} урона.\n\n'
        update('mob_current', 'health', health, idvk)
        print(f'Mob was attacked and got {damage} damage by player {idvk}')
    else:
        status += f'\n⚒Вы не смогли пробить броню. Нанесено 0 урона\n'
        print(f'Mob was attacked and not got damage by player {idvk}')
    if (player[0]["attack"] > 1):
        update('player_current', 'attack', player[0]["attack"]-1, idvk)
    if (mob[0]["defence"] > 0 ):
        update('mob_current', 'defence', mob[0]["defence"]-1, idvk)
    return result


def mob_attack_defence(idvk):
    #атака моба
    player = select('mob_current', 'attack', idvk)
    mob = select('player_current','health, defence', idvk)
    damage = player[0]["attack"] - mob[0]["defence"]
    status = ""
    result = 0
    if (damage > 0):
        health = mob[0]["health"] - damage
        status = f'\n\n⚔Моб нанес {damage} урона.\n\n'
        result = damage
        update('player_current', 'health', health, idvk)
        print(f'Mob doing attack and took {damage} damage for player {idvk}')
    else:
        status += f'\n⚒Моб не смог пробить броню. Нанесено 0 урона\n'
        print(f'Mob doing attack and not took damage for player {idvk}')
        result = 0
    if (player[0]["attack"] > 1):
        update('mob_current', 'attack', player[0]["attack"]-1, idvk)
    if (mob[0]["defence"] > 0 ):
        update('player_current', 'defence', mob[0]["defence"]-1, idvk)
    return result

def player_turn(idvk):
    #Ход игрока
    costattack = select('setting', 'costattack', idvk)
    playerdex = select('player_current', 'dexterity', idvk)
    status = ""
    turns = 0
    damage = 0
    dexterity = playerdex[0]["dexterity"]
    while (dexterity >= costattack[0]["costattack"]):
        print(f'Now turn player by {idvk}')
        damage = player_attack_defence(idvk)
        update('player_current', 'dexterity', dexterity - costattack[0]["costattack"], idvk)
        playerdex = select('player_current', 'dexterity', idvk)
        dexterity = playerdex[0]["dexterity"]
        #проверка победы игрока
        winner = player_win_bool(idvk)
        turns += turns + 1
        if (winner == True):
            status += f'\n\nВы нанесли {damage} x{turns}\n\n'
            return status
    status += f'\n\nВы нанесли {damage} x{turns}\n\n'
    return status

def mob_turn(idvk):
    mobname = f'Синий слизень'
    costattack = select('setting', 'costattack', idvk)
    mobdex = select('mob_current', 'dexterity', idvk)
    status = ""
    turns = 0
    damage = 0
    while (mobdex[0]["dexterity"] >= costattack[0]["costattack"]):
        print(f'Now turn mob for {idvk}')
        damage = mob_attack_defence(idvk)
        turns = turns + 1
        update('mob_current', 'dexterity', mobdex[0]["dexterity"] - costattack[0]["costattack"], idvk)
        mobdex = select('mob_current', 'dexterity', idvk)
        #проверка на смерть игрока
        winner = player_dead(idvk)
        if (winner != False):
            status += f'\n\n{mobname} нанес {damage} x{turns}\n\n'
            return status
    status += f'\n\n{mobname} нанес {damage} x{turns}\n\n'
    return status

def battle_add_energy(idvk):
    costattack = select('setting', 'costattack', idvk)
    playerdex = select('player_current', 'dexterity', idvk)
    mobdex = select('mob_current', 'dexterity', idvk)
    player = select('player', 'dexterity', idvk)
    mob = select('mob', 'dexterity', idvk)
    status = ""
    if (playerdex[0]["dexterity"] < costattack[0]["costattack"] and mobdex[0]["dexterity"] < costattack[0]["costattack"]):
        print(f'End turn for player and mob by {idvk}')
        playerdex = select('player_current', 'dexterity', idvk)
        mobdex = select('mob_current', 'dexterity', idvk)
        runes = select_equip('rune', 'SUM(dexterity)', idvk)
        if (runes[0]["SUM(dexterity)"] != None):
            update('player_current', 'dexterity', playerdex[0]["dexterity"]+player[0]["dexterity"]+runes[0]["SUM(dexterity)"], idvk)
        else:
            update('player_current', 'dexterity', playerdex[0]["dexterity"]+player[0]["dexterity"], idvk)
        update('mob_current', 'dexterity', mobdex[0]["dexterity"]+mob[0]["dexterity"], idvk)
        if (runes[0]["SUM(dexterity)"] != None):
            status += f'\n\n⚡Вы восстановили {player[0]["dexterity"]+runes[0]["SUM(dexterity)"]} энергии\n'
        else:
            status += f'\n\n⚡Вы восстановили {player[0]["dexterity"]} энергии\n'
        status += f'⚡Моб восстановил {mob[0]["dexterity"]} энергии\n\n'
        status += print_battle_turn_mob(idvk)
        status += print_battle_turn_player(idvk)
        return status
    return status

def player_turn_return(idvk):
    costattack = select('setting', 'costattack', idvk)
    playerdex = select('player_current', 'dexterity', idvk)
    status = ""
    if (playerdex[0]["dexterity"] >= costattack[0]["costattack"]):
        #передача управления игроку
        status += print_battle_turn_mob(idvk)
        status += print_battle_turn_player(idvk)
        return status
    return False

def player_max_lvl_killed(idvk):
    maxlvl = select('setting', 'lvlmobkilled', idvk)
    mob = select('mob', 'lvl', idvk)
    if (maxlvl[0]["lvlmobkilled"] < mob[0]["lvl"]):
        update('setting', 'lvlmobkilled', mob[0]["lvl"], idvk)
        print(f'Reach new max lvl {mob[0]["lvl"]} from killing mobs {idvk}')

def player_win(idvk):
    mob = select('mob_current', 'health', idvk)
    status = ""
    if (mob[0]["health"] <= 0):
        status += f'👊🏻Вы прикончили моба'
        status += player_lvl_up(idvk)
        moblvl = select('mob', 'lvl', idvk)
        if (moblvl[0]["lvl"] > 0):
            player_max_lvl_killed(idvk)
            genrune = generate_rune(idvk)
            if (genrune != False):
                status += genrune
                status += print_rune_last_gen(idvk)
        return status
    return False

def player_win_bool(idvk):
    mob = select('mob_current', 'health', idvk)
    if (mob[0]["health"] <= 0):
        return True
    return False

def player_dead(idvk):
    player = select('player_current', 'health', idvk)
    status = ""
    if (player[0]["health"] <= 0):
        status += f'☠Вы умерли'
        return status
    return False
    
def battle_control(idvk):
    #контролер битвы
    mobcheck = select('mob_current', 'health', idvk)
    playercheck = select('player_current', 'health', idvk)
    status = ""
    if (mobcheck[0]["health"] <= 0 or playercheck[0]["health"] <= 0):
        status += f'\n\nВы бьете воздух, как насчет исследовать дальше?\n'
        status += f'P.s. жмите кнопку "Исследовать" или повысьте здоровье\n'
        return status
    player = select('player', 'dexterity', idvk)
    mob = select('mob', 'dexterity', idvk)
    runes = select_equip('rune', 'SUM(dexterity)', idvk)
    dex = player[0]["dexterity"]
    if (runes[0]["SUM(dexterity)"] != None):
        dex = dex + runes[0]["SUM(dexterity)"]
    status = ""
    if (dex >= mob[0]["dexterity"]):
        #атака игрока с преобладающей ловкостью
        status += player_turn(idvk)
        #проверка победы игрока
        winner = player_win(idvk)
        if (winner != False):
            status += winner
            return status
        #проверка на передачу хода игроку
        """check = player_turn_return(idvk)
        if (check != False):
            status += check
            return status"""
        #атака моба
        status += mob_turn(idvk)
        #проверка на смерть игрока
        winner = player_dead(idvk)
        if (winner != False):
            status += winner
            return status
        #начисление энергии
        status += battle_add_energy(idvk)
        return status
    else:
        #атака моба по игроку
        status += mob_turn(idvk)
        #проверка на смерть игрока
        winner = player_dead(idvk)
        if (winner != False):
            status += winner
            return status
        #атака игрока по мобу
        status += player_turn(idvk)
        #проверка победы игрока
        winner = player_win(idvk)
        if (winner != False):
            status += winner
            return status
        #проверка на передачу хода игроку
        """check = player_turn_return(idvk)
        if (check != False):
            status += check
            return status"""
        #Начисление энергии
        status += battle_add_energy(idvk)
        return status

def lvl_next(idvk):
    #смена локации вверх
    lvlloc = select('setting', 'lvl', idvk)
    lvl = lvlloc[0]["lvl"]
    update('setting', 'lvl', lvl+1, idvk)
    print(f'Level next on {lvl+1} for {idvk}')
    status = f'📝Вы прошли вглубь в лес на {lvl+1} аршина'
    return status

def lvl_down(idvk):
    #смена локации вниз
    lvlloc = select('setting', 'lvl', idvk)
    lvl =lvlloc[0]["lvl"]
    if (lvl >= 1):
        update('setting', 'lvl', lvl-1, idvk)
        print(f'Level down on {lvl} for {idvk}')
        status = f'📝Вы пошли в сторону света на {lvl-1} аршина'
        return status
    status = f'Никто, асбсолютно никто там еще не был!'
    return status

def player_lvl_up(idvk):
    player = select('player', 'xp, lvl, points, gold', idvk)
    mob = select('mob', 'xp, gold', idvk)
    lvl = player[0]["lvl"]
    xp = player[0]["xp"]
    xp = xp + mob[0]["xp"]
    status = ""
    if ((50+(10*lvl)*lvl) <= xp):
        update('player', 'lvl', lvl+1, idvk)
        status += f'\n\n📝Вы достигли уровня {lvl+1}\n\n'
        print(f'Level up on {lvl+1} for player {idvk}')
        update('player', 'xp', xp - (50+(10*lvl)*lvl), idvk)
        update('player', 'points', player[0]["points"]+1, idvk)
        status += f'\n\n🌟Вы получили 1 очко навыков\n\n'
        print(f'Got 1 point player {idvk}')
        return status
    update('player', 'xp', xp, idvk)
    status += f'\n\n📗Вы получили {mob[0]["xp"]} опыта\n\n'
    print(f'From mob got {mob[0]["xp"]} xp for player {idvk}')
    if (random.SystemRandom(100).randint(0,100) < 30):
        update('player', 'gold', player[0]["gold"]+mob[0]["gold"], idvk)
        status += f'🎆Вы получили {mob[0]["gold"]} рунной пыли'
        print(f'From mob got {mob[0]["gold"]} gold for player {idvk}')
    return status

def reward(idvk):
    #inventory = select('reward', 'lvl, points, gold', idvk)
    inventory = select('reward', 'lvl, points, gold, mythical, legendary, epic, rare, unusual, usual', idvk)
    runes = select('inventory', 'mythical, legendary, epic, rare, unusual, usual', idvk)
    mythical = runes[0]["mythical"] + inventory[0]["mythical"]
    status = f'\nНачислено {inventory[0]["mythical"]} мифических обломков\n'
    update('inventory', 'mythical', mythical, idvk)
    update('reward', 'mythical', 0, idvk)
    legendary = runes[0]["legendary"] + inventory[0]["legendary"]
    status += f'\nНачислено {inventory[0]["legendary"]} легендарных обломков\n'
    update('inventory', 'legendary', legendary, idvk)
    update('reward', 'legendary', 0, idvk)
    epic = runes[0]["epic"] + inventory[0]["epic"]
    status += f'\nНачислено {inventory[0]["epic"]} эпических обломков\n'
    update('inventory', 'epic', epic, idvk)
    update('reward', 'epic', 0, idvk)
    rare = runes[0]["rare"] + inventory[0]["rare"]
    status += f'\nНачислено {inventory[0]["rare"]} редких обломков\n'
    update('inventory', 'rare', rare, idvk)
    update('reward', 'rare', 0, idvk)
    unusual = runes[0]["unusual"] + inventory[0]["unusual"]
    status += f'\nНачислено {inventory[0]["rare"]} необычных обломков\n'
    update('inventory', 'unusual', unusual, idvk)
    update('reward', 'unusual', 0, idvk)
    usual = runes[0]["usual"] + inventory[0]["usual"]
    status += f'\nНачислено {inventory[0]["usual"]} обычных обломков\n'
    update('inventory', 'usual', usual, idvk)
    update('reward', 'usual', 0, idvk)
    player = select('player', 'lvl, points, gold', idvk)
    rew = player[0]["lvl"] + inventory[0]["lvl"]
    status += f'\nВаш уровень увеличен на {inventory[0]["lvl"]}\n'
    update('player', 'lvl', rew, idvk)
    update('reward', 'lvl', 0, idvk)
    reg = player[0]["gold"] + inventory[0]["gold"]
    status += f'\nРунная пыль начислена в количестве {inventory[0]["gold"]}\n'
    update('player', 'gold', reg, idvk)
    update('reward', 'gold', 0, idvk)
    rep = player[0]["points"] + inventory[0]["points"]
    status += f'\nОчки характеристик восстановлены до {inventory[0]["points"]} очков\n'
    update('player', 'points', rep, idvk)
    update('reward', 'points', 0, idvk)
    print(f'Sent {inventory[0]["points"]} xp and {inventory[0]["gold"]} for player {idvk}')
    return status

def rune_equip(idvk):
    #надевание руны
    rune = select('rune', 'id', idvk)
    item = select('setting', 'itemid', idvk)
    itemid = item[0]["itemid"]
    status = ""
    try:
        if (rune[itemid]["id"]):
            iditem = rune[itemid]["id"]
            check = select_item('rune', 'equip', idvk, iditem)
            if (check[0]["equip"] == "no"):
                update_item('rune', 'equip', "yes", idvk, iditem)
                status += f'\n\n🧿Руна {iditem} надета\n\n'
                print(f'Rune {iditem} equip by player {idvk}')
                return status
            else:
                status += f'\n\n🧿Руна {iditem} уже экипирована\n\n'
                print(f'Rune {iditem} already equip by player {idvk}')
                return status
    except:
        status += f'\n\nНе удалось надеть руну\n\n'
        print(f'Can not equip rune for player {idvk}')
        return status


def rune_unequip(idvk):
    #снятие руны
    rune = select('rune', 'id', idvk)
    item = select('setting', 'itemid', idvk)
    itemid = item[0]["itemid"]
    status = ""
    try:
        if (rune[itemid]["id"]):
            iditem = rune[itemid]["id"]
            check = select_item('rune', 'equip', idvk, iditem)
            if (check[0]["equip"] == "yes"):
                update_item('rune', 'equip', "no", idvk, iditem)
                status += f'\n\n🧿Руна {iditem} снята\n\n'
                print(f'Rune {iditem} unequip by player {idvk}')
                return status
            else:
                status += f'\n\n🧿Руна {iditem} не была экипирована\n\n'
                print(f'Rune {iditem} already unequip by player {idvk}')
                return status
    except:
        status += f'\n\nНе удалось снять руну\n\n'
        print(f'Can not unequip rune for player {idvk}')
        return status

def rune_next(idvk):
    #следующая руна
    rune = select('rune', 'id', idvk)
    item = select('setting', 'itemid', idvk)
    itemid = item[0]["itemid"]+1
    status = ""
    try:
        if (rune[itemid]["id"] and itemid <= 20):
            iditem = rune[itemid]["id"]
            check = select_item('rune', 'id', idvk, iditem)
            if (check[0]["id"] == iditem):
                update('setting', 'itemid', itemid, idvk)
                status += f'\n\nСледующая руна:\n\n'
                status += print_rune(idvk)
                print(f'Rune {iditem} will next for player {idvk}')
                return status
            else:
                status += f'\n\n🧿Руна {iditem} не обнаружена.\n\n'
                print(f'Rune {iditem} not be for player {idvk}')
                return status
    except:
        status += f'\n\nСледующая рунна не обнаружена, переход к первому предмету.\n\n'
        update('setting', 'itemid', 0, idvk)
        status += print_rune(idvk)
        print(f'Not found next rune for player {idvk}')
        return status

def rune_down(idvk):
    #предыдущая руна
    rune = select('rune', 'id', idvk)
    item = select('setting', 'itemid', idvk)
    itemid = item[0]["itemid"]-1
    status = ""
    try:
        if (rune[itemid]["id"] and itemid <= 20 and itemid >= 0):
            iditem = rune[itemid]["id"]
            check = select_item('rune', 'id', idvk, iditem)
            if (check[0]["id"] == iditem):
                update('setting', 'itemid', itemid, idvk)
                status += f'\n\nПредыдущая руна:\n\n'
                status += print_rune(idvk)
                print(f'Rune {iditem} will down for player {idvk}')
                return status
            else:
                status += f'\n\n🧿Руна {iditem} не обнаружена.\n\n'
                print(f'Rune {iditem} down not be for player {idvk}')
                return status
    except:
        status += f'\n\nПредыдущая рунна не обнаружена, переход к последнему элементу предмету.\n\n'
        update('setting', 'itemid', 0, idvk)
        status += print_rune(idvk)
        print(f'Not found down rune for player {idvk}')
        return status
    count = select('rune', 'COUNT(id)', idvk)
    status += f'\n\nПредыдущая рунна не обнаружена, переход к последнему предмету.\n\n'
    update('setting', 'itemid', count[0]["COUNT(id)"]-1, idvk)
    status += print_rune(idvk)
    print(f'Not found down rune for player {idvk}')
    return status

def rune_destroy(idvk, iditem):
    #разпушение руны
    rune = select_item('rune', 'attack, defence, defencemagic, dexterity, intelligence, health', idvk, iditem)
    attack = rune[0]["attack"]
    defence = rune[0]["defence"]
    defencemagic = rune[0]["defencemagic"]
    dexterity = rune[0]["dexterity"]
    intelligence = rune[0]["intelligence"]
    health = rune[0]["health"]
    points = 0
    status = f'\n\nРуна {iditem} разрушена:\n'
    if (attack != 0):
        points = points + 1
    if (defence != 0):
        points = points + 1
    if (defencemagic != 0):
        points = points + 1
    if (dexterity != 0):
        points = points + 1
    if (intelligence != 0):
        points = points + 1
    if (health != 0):
        points = points + 1
    if (points == 1):
        target = f'usual'
        status += f'\nВы получили обычный обломок\n'
    if (points == 2):
        target = f'unusual'
        status += f'\nВы получили необычный обломок\n'
    if (points == 3):
        target = f'rare'
        status += f'\nВы получили редкий обломок\n'
    if (points == 4):
        target = f'epic'
        status += f'\nВы получили эпический обломок\n'
    if (points == 5):
        target = f'legendary'
        status += f'\nВы получили легендарный обломок\n'
    if (points == 6):
        target = f'mythical'
        status += f'\nВы получили мифический обломок\n'
    destroy = select('inventory', target, idvk)
    update('inventory', target, destroy[0][target]+1, idvk)
    print(f'Rune {target} destroy for player {idvk}')
    return status

def rune_delete(idvk):
    #распыление руны
    rune = select('rune', 'id', idvk)
    item = select('setting', 'itemid', idvk)
    itemid = item[0]["itemid"]
    status = ""
    try:
        if (rune[itemid]["id"]):
            iditem = rune[itemid]["id"]
            check = select_item('rune', 'id', idvk, iditem)
            if (check[0]["id"] == iditem):
                status += rune_destroy(idvk, iditem)
                check = delete_item('rune', idvk, iditem)
                status += f'\nТекущая руна:\n'
                #update('setting', 'itemid', iditem, idvk)
                #status += print_rune(idvk)
                status += rune_down(idvk)
                print(f'Rune {iditem} was destroy for player {idvk}')
                return status
            else:
                status += f'\n\n🧿Руна {iditem} не обнаружена.\n\n'
                print(f'Rune {iditem} not destroy for player {idvk}')
                return status
    except:
        status += f'\n\nРуна не обнаружена для распыления.\n\n'
        print(f'Not found rune for destroy by player {idvk}')
        return status
    return f'Руна не разрушена'

def use_runes_equip(idvk):
    runes = select_equip('rune', 'SUM(attack), SUM(defence), SUM(defencemagic), SUM(dexterity), SUM(intelligence), SUM(health)', idvk)
    if (runes[0]["SUM(attack)"] != None):
        player = select('player_current', 'attack, defence, defencemagic, dexterity, intelligence, health, mana', idvk)
        attack = player[0]["attack"] + runes[0]["SUM(attack)"]
        update('player_current', 'attack', attack, idvk)
        defence = player[0]["defence"] + runes[0]["SUM(defence)"]
        update('player_current', 'defence', defence, idvk)
        defencemagic = player[0]["defencemagic"] + runes[0]["SUM(defencemagic)"]
        update('player_current', 'defencemagic', defencemagic, idvk)
        dexterity = player[0]["dexterity"] + runes[0]["SUM(dexterity)"]
        update('player_current', 'dexterity', dexterity, idvk)
        intelligence = player[0]["intelligence"] + runes[0]["SUM(intelligence)"]
        update('player_current', 'intelligence', intelligence, idvk)
        health = player[0]["health"] + runes[0]["SUM(health)"]
        update('player_current', 'health', health, idvk)
        mana = player[0]["mana"] + runes[0]["SUM(intelligence)"]
        update('player_current', 'mana', mana, idvk)
        print(f'Runes activated for player {idvk}')
    
def reseach(idvk):
    delete('mob_current',idvk)
    delete('player_current',idvk)
    delete('mob',idvk)
    generate_mob(idvk)
    generate_battle(idvk)
    use_runes_equip(idvk)
    costattack = battle_dexterity_equal(idvk)
    print(f'Price for attack {costattack} by player {idvk}')
    update('setting', 'costattack', costattack, idvk)
    status = print_mob_profile(idvk)
    return status

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

def print_profile(idvk):
    #вывод профиля
    runes = select_equip('rune', 'SUM(attack), SUM(defence), SUM(defencemagic), SUM(dexterity), SUM(intelligence), SUM(health)', idvk)
    if (runes[0]["SUM(attack)"] != None):
        profile = select('player', 'lvl, xp, gold, points, attack, defence, defencemagic, dexterity, intelligence, health', idvk)
        attack = runes[0]["SUM(attack)"]
        defence = runes[0]["SUM(defence)"]
        defencemagic = runes[0]["SUM(defencemagic)"]
        dexterity = runes[0]["SUM(dexterity)"]
        intelligence = runes[0]["SUM(intelligence)"]
        health = runes[0]["SUM(health)"]
        result = f'\n\nВаш персонаж:\n'
        result = f' 📝Уровень: {profile[0]["lvl"]} \n'
        result += f' 📗Опыт: {profile[0]["xp"]}/{(50+(10*profile[0]["lvl"])*profile[0]["lvl"])} \n'
        result += f' 🎆Рунная пыль: {profile[0]["gold"]} \n\n'
        result += f' Здоровье: \n'
        result +=  f' ❤{profile[0]["health"] + health} ({profile[0]["health"]}🌟{health}🧿)  \n'
        result += f' Атака: \n'
        result +=  f' 🗡{profile[0]["attack"] + attack} ({profile[0]["attack"]}🌟{attack}🧿) \n'
        result += f' Физ. защита: \n'
        result +=  f' 🛡{profile[0]["defence"] + defence} ({profile[0]["defence"]}🌟{defence}🧿) \n'
        result += f' Маг. защита: \n'
        result +=  f' 🔰{profile[0]["defencemagic"] + defencemagic} ({profile[0]["defencemagic"]}🌟{defencemagic}🧿) \n'
        result += f' Ловкость: \n'
        result +=  f' 🦶{profile[0]["dexterity"] + dexterity} ({profile[0]["dexterity"]}🌟{dexterity}🧿) \n'
        result += f' Интеллект: \n'
        result +=  f' 🌀{profile[0]["intelligence"] + intelligence} ({profile[0]["intelligence"]}🌟{intelligence}🧿) \n\n'
        result += f' 🌟Очки параметров: {profile[0]["points"]} \n\n'
    else:
        profile = select('player', 'lvl, xp, gold, points, attack, defence, defencemagic, dexterity, intelligence, health', idvk)
        result = f'\n\nВаш персонаж:\n'
        result = f' 📝Уровень: {profile[0]["lvl"]} \n'
        result += f' 📗Опыт: {profile[0]["xp"]}/{(50+(10*profile[0]["lvl"])*profile[0]["lvl"])} \n'
        result += f' 🎆Рунная пыль: {profile[0]["gold"]} \n\n'
        result += f' ❤Здоровье: {profile[0]["health"]} \n'
        result += f' 🗡Атака: {profile[0]["attack"]} \n'
        result += f' 🛡Физ. защита: {profile[0]["defence"]} \n'
        result += f' 🔰Маг. защита: {profile[0]["defencemagic"]} \n'
        result += f' 🦶Ловкость: {profile[0]["dexterity"]} \n'
        result += f' 🌀Интеллект: {profile[0]["intelligence"]} \n\n'
        result += f' 🌟Очки параметров: {profile[0]["points"]} \n\n'
    print(f'Print profile for {idvk}.')
    return str(result)

def print_mob_profile(idvk):
    #вывод профиля мобв
    mobname = f'Синий слизень'
    profile = select('mob', 'lvl, xp, gold, points, attack, defence, defencemagic, dexterity, intelligence, health', idvk)
    result = f'\n\n{mobname}:\n'
    result += f' 📝Уровень: {profile[0]["lvl"]} \n'
    result += f' 📗Опыт: {profile[0]["xp"]} \n'
    result += f' 🎆Рунная пыль: {profile[0]["gold"]} \n\n'
    result += f' ❤Здоровье: {profile[0]["health"]} \n'
    result += f' 🗡Атака: {profile[0]["attack"]} \n'
    result += f' 🛡Физ. защита: {profile[0]["defence"]} \n'
    result += f' 🔰Маг. защита: {profile[0]["defencemagic"]} \n'
    result += f' 🦶Ловкость: {profile[0]["dexterity"]} \n'
    result += f' 🌀Интеллект: {profile[0]["intelligence"]} \n\n'
    #result += f' 🌟Очки параметров:{profile[0]["points"]} '
    print(f'Print mob for {idvk}.')
    return str(result)

def back(idvk):
    #путь назад
    status = f'Ничего не предвещало беды...'
    return str(status)

def altar(idvk):
    #путь назад
    status = f'Возможно именно здесь была создана первая руна...'
    return str(status)

def command_attack(idvk):
    #проверка на ловкость
    battle_dexterity_equal(idvk)

def print_battle_turn_player(idvk):
    #конец хода игрока
    player = select('player', 'attack, defence, defencemagic, dexterity, intelligence, health', idvk)
    player_current = select('player_current', 'attack, defence, defencemagic, dexterity, intelligence, health, mana', idvk)
    runes = select_equip('rune', 'SUM(attack), SUM(defence), SUM(defencemagic), SUM(dexterity), SUM(intelligence), SUM(health)', idvk)
    costattack = select('setting', 'costattack', idvk)
    if (runes[0]["SUM(attack)"] != None):
        status = f'\n\nВы:\n'
        status += f' ❤{player_current[0]["health"]}/{player[0]["health"]+runes[0]["SUM(health)"]} '
        status += f' 🛡{player_current[0]["defence"]}/{player[0]["defence"]+runes[0]["SUM(defence)"]} '
        status += f'⚡{player_current[0]["dexterity"]}/{costattack[0]["costattack"]} \n'
        status += f' 🗡{player_current[0]["attack"]}/{player[0]["attack"]+runes[0]["SUM(attack)"]} ' 
        status += f' 🔰{player_current[0]["defencemagic"]}/{player[0]["defencemagic"]+runes[0]["SUM(defencemagic)"]} '
        status += f'🔷{player_current[0]["mana"]}/{player[0]["intelligence"]*4+runes[0]["SUM(intelligence)"]} \n\n'
    else:
        status = f'\n\nВы:\n'
        status += f' ❤{player_current[0]["health"]}/{player[0]["health"]} '
        status += f' 🛡{player_current[0]["defence"]}/{player[0]["defence"]} '
        status += f'⚡{player_current[0]["dexterity"]}/{costattack[0]["costattack"]} \n'
        status += f' 🗡{player_current[0]["attack"]}/{player[0]["attack"]} ' 
        status += f' 🔰{player_current[0]["defencemagic"]}/{player[0]["defencemagic"]} '
        status += f'🔷{player_current[0]["mana"]}/{player[0]["intelligence"]*2} \n\n'
    print(f'Print battle panel about player for {idvk}')
    return status

def print_battle_turn_mob(idvk):
    #конец хода моба
    mobname = f'Синий слизень'
    player = select('mob', 'attack, defence, defencemagic, dexterity, intelligence, health', idvk)
    player_current = select('mob_current', 'attack, defence, defencemagic, dexterity, intelligence, health, mana', idvk)
    costattack = select('setting', 'costattack', idvk)
    status = f'\n\n{mobname}:\n'
    status += f' ❤{player_current[0]["health"]}/{player[0]["health"]} '
    status += f' 🛡{player_current[0]["defence"]}/{player[0]["defence"]} '
    status += f'⚡{player_current[0]["dexterity"]}/{costattack[0]["costattack"]} \n'
    status += f' 🗡{player_current[0]["attack"]}/{player[0]["attack"]} ' 
    status += f' 🔰{player_current[0]["defencemagic"]}/{player[0]["defencemagic"]} '
    status += f'🔷{player_current[0]["mana"]}/{player[0]["intelligence"]*2} \n\n'
    print(f'Print battle panel about mob for {idvk}')
    return status

def print_rune_last_gen(idvk):
    #вывод руны
    player = select('rune', 'id, lvl, attack, defence, defencemagic, dexterity, intelligence, health', idvk)
    attack = player[-1]["attack"]
    defence = player[-1]["defence"]
    defencemagic = player[-1]["defencemagic"]
    dexterity = player[-1]["dexterity"]
    intelligence = player[-1]["intelligence"]
    health = player[-1]["health"]
    status = f'\n\n🧿Руна {player[-1]["id"]}\n'
    status += f'📝Уровень: {player[-1]["lvl"]} \n'
    if (health != 0):
        status += f'❤Здоровье: {health}\n'
    if (attack != 0):
        status += f'🗡Атака: {attack}\n'
    if (defence != 0):
        status += f'🛡Физ. защ: {defence}\n'
    if (defencemagic != 0):
        status += f'🔰Маг. защ: {defencemagic}\n'
    if (dexterity != 0):
        status += f'🦶Ловкость: {dexterity}\n'
    if (intelligence != 0):
        status += f'🌀Интеллект: {intelligence}\n\n'
    print(f'Print generated rune for {idvk}')
    return status

def print_rune(idvk):
    rune = select('rune', 'id', idvk)
    item = select('setting', 'itemid', idvk)
    itemid = item[0]["itemid"]
    status = ""
    try:
        if (rune[itemid]["id"]):
            iditem = rune[itemid]["id"]
            player = select_item('rune', 'id, lvl, attack, defence, defencemagic, dexterity, intelligence, health', idvk, iditem)
            attack = player[0]["attack"]
            defence = player[0]["defence"]
            defencemagic = player[0]["defencemagic"]
            dexterity = player[0]["dexterity"]
            intelligence = player[0]["intelligence"]
            health = player[0]["health"]
            status = f'\n\n🧿Руна {player[0]["id"]}\n'
            status += f'📝Уровень: {player[0]["lvl"]} \n'
            if (health != 0):
                status += f'❤Здоровье: {health}\n'
            if (attack != 0):
                status += f'🗡Атака: {attack}\n'
            if (defence != 0):
                status += f'🛡Физ. защ: {defence}\n'
            if (defencemagic != 0):
                status += f'🔰Маг. защ: {defencemagic}\n'
            if (dexterity != 0):
                status += f'🦶Ловкость: {dexterity}\n'
            if (intelligence != 0):
                status += f'🌀Интеллект: {intelligence}\n\n'
            print(f'Print current rune for {idvk}')
            return status
    except:
        check = select('rune', 'id', idvk)
        try:
            if (check[0]["id"] != None):
                status += f'Нажмите +руна, чтобы перейти к первой руне.'
                return status
        except:
            status += f'У вас пока что нет рун'
            print(f'Not found rune for player {idvk}')
            return status
    status += f'У вас пока что нет рун'
    print(f'Not found rune for player {idvk}')
    return status

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
    player = select('player_current', 'dexterity', idvk)
    mob = select('mob', 'dexterity', idvk)
    if (player[0]["dexterity"] > mob[0]["dexterity"]):
        return mob[0]["dexterity"]
    else:
        return player[0]["dexterity"]