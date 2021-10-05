from os import urandom
import random
from modules.sqlite.connect import con
from modules.sqlite.engine import generate_rune
from modules.sqlite.engine.printer import print_battle_turn_mob, print_battle_turn_player, print_rune, print_rune_last_gen
from modules.sqlite.engine.select import *
from modules.sqlite.engine.delete import *
import datetime
#Запросы на апдейт новых данных

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
    if (damage > 0):
        health = mob[0]["health"] - damage
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
    return status


def mob_attack_defence(idvk):
    #атака моба
    player = select('mob_current', 'attack', idvk)
    mob = select('player_current','health, defence', idvk)
    damage = player[0]["attack"] - mob[0]["defence"]
    status = ""
    if (damage > 0):
        health = mob[0]["health"] - damage
        status += f'\n\n⚔Моб нанес {damage} урона.\n\n'
        update('player_current', 'health', health, idvk)
        print(f'Mob doing attack and took {damage} damage for player {idvk}')
    else:
        status += f'\n⚒Моб не смог пробить броню. Нанесено 0 урона\n'
        print(f'Mob doing attack and not took damage for player {idvk}')
    if (player[0]["attack"] > 1):
        update('mob_current', 'attack', player[0]["attack"]-1, idvk)
    if (mob[0]["defence"] > 0 ):
        update('player_current', 'defence', mob[0]["defence"]-1, idvk)
    return status

def player_turn(idvk):
    #Ход игрока
    costattack = select('setting', 'costattack', idvk)
    playerdex = select('player_current', 'dexterity', idvk)
    status = ""
    while (playerdex[0]["dexterity"] >= costattack[0]["costattack"]):
        print(f'Now turn player by {idvk}')
        status += player_attack_defence(idvk)
        update('player_current', 'dexterity', playerdex[0]["dexterity"] - costattack[0]["costattack"], idvk)
        playerdex = select('player_current', 'dexterity', idvk)
        #проверка победы игрока
        winner = player_win_bool(idvk)
        if (winner != False):
            return status
        return status
    return status

def mob_turn(idvk):
    costattack = select('setting', 'costattack', idvk)
    mobdex = select('mob_current', 'dexterity', idvk)
    status = ""
    while (mobdex[0]["dexterity"] >= costattack[0]["costattack"]):
        print(f'Now turn mob for {idvk}')
        status += mob_attack_defence(idvk)
        update('mob_current', 'dexterity', mobdex[0]["dexterity"] - costattack[0]["costattack"], idvk)
        mobdex = select('mob_current', 'dexterity', idvk)
        #проверка на смерть игрока
        winner = player_dead(idvk)
        if (winner != False):
            return status
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
        update('player_current', 'dexterity', playerdex[0]["dexterity"]+player[0]["dexterity"], idvk)
        update('mob_current', 'dexterity', mobdex[0]["dexterity"]+mob[0]["dexterity"], idvk)
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

def player_win(idvk):
    mob = select('mob_current', 'health', idvk)
    status = ""
    if (mob[0]["health"] <= 0):
        status += f'👊🏻Вы прикончили моба'
        status += player_lvl_up(idvk)
        moblvl = select('mob', 'lvl', idvk)
        if (moblvl[0]["lvl"] > 0):
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
        status += f'P.s. жмите кнопку "Исследовать".\n Иначе вам нужно распределить очки в здоровье через "Профиль"\n\n'
        return status
    player = select('player', 'dexterity', idvk)
    mob = select('mob', 'dexterity', idvk)
    status = ""
    if (player[0]["dexterity"] >= mob[0]["dexterity"]):
        #атака игрока с преобладающей ловкостью
        status += player_turn(idvk)
        #проверка победы игрока
        winner = player_win(idvk)
        if (winner != False):
            status += winner
            return status
        #проверка на передачу хода игроку
        check = player_turn_return(idvk)
        if (check != False):
            status += check
            return status
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
        check = player_turn_return(idvk)
        if (check != False):
            status += check
            return status
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
    reward = select('reward', 'xp, gold', idvk)
    player = select('player', 'xp, gold', idvk)
    rew = player[0]["xp"] + reward[0]["xp"]
    update('player', 'xp', rew, idvk)
    update('reward', 'xp', 0, idvk)
    reg = player[0]["gold"] + reward[0]["gold"]
    update('player', 'gold', reg, idvk)
    update('reward', 'gold', 0, idvk)
    status = f'\n\n📗{idvk}, вам начислено {reward[0]["xp"]} опыта\n'
    status += f'📗{idvk}, вам начислено {reward[0]["gold"]} рунной пыли\n\n'
    print(f'Sent {reward[0]["xp"]} xp and {reward[0]["gold"]} for player {idvk}')
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
    print(f'0')
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
                status += print_rune(idvk)
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
    