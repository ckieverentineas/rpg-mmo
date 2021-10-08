import sqlite3
from modules.sqlite.connect import con
#запросы к базам данных
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

def print_rune_last_gen(idvk):
    #вывод руны
    player = select('rune', 'id, attack, defence, defencemagic, dexterity, intelligence, health', idvk)
    attack = player[-1]["attack"]
    defence = player[-1]["defence"]
    defencemagic = player[-1]["defencemagic"]
    dexterity = player[-1]["dexterity"]
    intelligence = player[-1]["intelligence"]
    health = player[-1]["health"]
    status = f'\n\n🧿Руна {player[-1]["id"]}\n'
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
