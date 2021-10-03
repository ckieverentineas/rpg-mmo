from os import urandom
import random
from modules.sqlite.connect import con
from modules.sqlite.engine.printer import print_battle_turn_mob, print_battle_turn_player
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
    status += f'Начислено {int(point)} очков параметров.'
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
        status += f'\n\nВы нанесли {damage} урона.\n\n'
        update('mob_current', 'health', health, idvk)
        print(f'Mob was attacked and got {damage} damage by player {idvk}')
    else:
        status += f'\nВы не смогли пробить броню. Нанесено 0 урона\n'
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
        status += f'\n\nМоб нанес {damage} урона.\n\n'
        update('player_current', 'health', health, idvk)
        print(f'Mob doing attack and took {damage} damage for player {idvk}')
    else:
        status += f'\nМоб не смог пробить броню. Нанесено 0 урона\n'
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
        status = player_attack_defence(idvk)
        update('player_current', 'dexterity', playerdex[0]["dexterity"] - costattack[0]["costattack"], idvk)
        playerdex = select('player_current', 'dexterity', idvk)
        #проверка победы игрока
        winner = player_win(idvk)
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
        status += f'\n\nВы восстановили {player[0]["dexterity"]} энергии\n'
        status += f'Моб восстановил {mob[0]["dexterity"]} энергии\n\n'
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
        status += f'Вы прикончили моба, как карася'
        status += player_lvl_up(idvk)
        return status
    return False

def player_dead(idvk):
    player = select('player_current', 'health', idvk)
    status = ""
    if (player[0]["health"] <= 0):
        status += f'Вы умерли'
        return status
    return False
    
def battle_control(idvk):
    #контролер битвы
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
    status = f'Вы прошли вглубь в лес на {lvl+1} аршина'
    return status

def lvl_down(idvk):
    #смена локации вниз
    lvlloc = select('setting', 'lvl', idvk)
    lvl =lvlloc[0]["lvl"]
    if (lvl >= 1):
        update('setting', 'lvl', lvl-1, idvk)
        print(f'Level down on {lvl} for {idvk}')
        status = f'Вы пошли в сторону света на {lvl-1} аршина'
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
        status += f'\n\nВы достигли уровня {lvl+1}\n\n'
        print(f'Level up on {lvl+1} for player {idvk}')
        update('player', 'xp', xp - (50+(10*lvl)*lvl), idvk)
        update('player', 'points', player[0]["points"]+1, idvk)
        status += f'\n\nВы получили 1 очко навыков\n\n'
        print(f'Got 1 point player {idvk}')
        return status
    update('player', 'xp', xp, idvk)
    status += f'\n\nВы получили {mob[0]["xp"]} опыта\n\n'
    print(f'From mob got {mob[0]["xp"]} xp for player {idvk}')
    if (random.SystemRandom(100).randint(0,100) < 30):
        update('player', 'gold', player[0]["gold"]+mob[0]["gold"], idvk)
        status += f'Вы получили {mob[0]["gold"]} рунной пыли'
        print(f'From mob got {mob[0]["gold"]} gold for player {idvk}')
    return status

def reward(idvk):
    reward = select('reward', 'xp', idvk)
    player = select('player', 'xp', idvk)
    rew = player[0]["xp"] + reward[0]["xp"]
    update('player', 'xp', rew, idvk)
    update('reward', 'xp', 0, idvk)
    status = f'{idvk}, вам начислено {reward[0]["xp"]} опыта'
    print(f'Sent {reward[0]["xp"]} xp for player {idvk}')
    return status
