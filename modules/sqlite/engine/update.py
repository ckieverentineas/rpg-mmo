from modules.sqlite.connect import con
from modules.sqlite.engine.select import *
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
    status += gen_status('Атака', stat)
    # обнуляем физическую защиту
    stat = source[0]["defence"]
    point = point + stat/3
    update('player','defence', 0, idvk)
    status += gen_status('Физическая защита', stat)
    # обнуляем защиту
    stat = source[0]["defencemagic"]
    point = point + stat/3
    update('player','defencemagic', 0, idvk)
    status += gen_status('Магическая защита', stat)
    #обнуляем ловкость
    stat = source[0]["dexterity"]
    point = point + stat/2
    update('player','dexterity', 0, idvk)
    status += gen_status('Ловкость', stat)
    #обнуляем интеллект
    stat = source[0]["intelligence"]
    point = point + stat/2
    update('player','intelligence', 0, idvk)
    status += gen_status('Интеллект', stat)
    #обнуляем здоровье
    stat = source[0]["health"]
    if (stat > 0):
        point = point + stat/4
    update('player','health', 0, idvk)
    status += gen_status('Здоровье', stat)
    #начисляем очки
    points = points + int(point)
    update('player', 'points', points, idvk)
    status += f'Начислено {int(point)} очков параметров.'
    print(f'Return {int(point)} for rebalance avatar by {idvk}.')
    return status