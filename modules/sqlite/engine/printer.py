from modules.sqlite.engine.add import *
from modules.sqlite.engine.select import *
#Выводы данных из баз данных
def print_profile(idvk):
    #вывод профиля
    runes = select_equip('rune', 'SUM(attack), SUM(defence), SUM(defencemagic), SUM(dexterity), SUM(intelligence), SUM(health)', idvk)
    if (runes[0]["SUM(attack)"] != None):
        profile = select('player', 'lvl, xp, gold, points, attack, defence, defencemagic, dexterity, intelligence, health', idvk)
        attack = runes[0]["SUM(attack)"]*2
        defence = runes[0]["SUM(defence)"]*3
        defencemagic = runes[0]["SUM(defencemagic)"]*3
        dexterity = runes[0]["SUM(dexterity)"]*2
        intelligence = runes[0]["SUM(intelligence)"]*2
        health = runes[0]["SUM(health)"]*4
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

def command_attack(idvk):
    #проверка на ловкость
    battle_dexterity_equal(idvk)

def print_battle_turn_player(idvk):
    #конец хода игрока
    player = select('player', 'attack, defence, defencemagic, dexterity, intelligence, health', idvk)
    player_current = select('player_current', 'attack, defence, defencemagic, dexterity, intelligence, health, mana', idvk)
    status = f'\n\nВы:\n'
    status += f' ❤{player_current[0]["health"]}/{player[0]["health"]} '
    status += f' 🛡{player_current[0]["defence"]}/{player[0]["defence"]} '
    status += f'⚡{player_current[0]["dexterity"]}/{player[0]["dexterity"]} \n'
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
    status = f'\n\n{mobname}:\n'
    status += f' ❤{player_current[0]["health"]}/{player[0]["health"]} '
    status += f' 🛡{player_current[0]["defence"]}/{player[0]["defence"]} '
    status += f'⚡{player_current[0]["dexterity"]}/{player[0]["dexterity"]} \n'
    status += f' 🗡{player_current[0]["attack"]}/{player[0]["attack"]} ' 
    status += f' 🔰{player_current[0]["defencemagic"]}/{player[0]["defencemagic"]} '
    status += f'🔷{player_current[0]["mana"]}/{player[0]["intelligence"]*2} \n\n'
    print(f'Print battle panel about mob for {idvk}')
    return status

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

def print_rune(idvk):
    rune = select('rune', 'id', idvk)
    item = select('setting', 'itemid', idvk)
    itemid = item[0]["itemid"]
    status = ""
    try:
        if (rune[itemid]["id"]):
            iditem = rune[itemid]["id"]
            player = select_item('rune', 'id, attack, defence, defencemagic, dexterity, intelligence, health', idvk, iditem)
            attack = player[0]["attack"]
            defence = player[0]["defence"]
            defencemagic = player[0]["defencemagic"]
            dexterity = player[0]["dexterity"]
            intelligence = player[0]["intelligence"]
            health = player[0]["health"]
            status = f'\n\n🧿Руна {player[0]["id"]}\n'
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