from modules.sqlite.engine.add import *
from modules.sqlite.engine.select import *
#Выводы данных из баз данных
def print_profile(idvk):
    #вывод профиля
    profile = select('player', 'lvl, xp, gold, points, attack, defence, defencemagic, dexterity, intelligence, health', idvk)
    result = f'\n\nВаш персонаж:\n'
    result = f' 📝Уровень:{profile[0]["lvl"]} \n'
    result += f' 📗Опыт:{profile[0]["xp"]} \n'
    result += f' 🎆Рунная пыль:{profile[0]["gold"]} \n\n'
    result += f' ❤Здоровье:{profile[0]["health"]} \n'
    result += f' 🗡Атака:{profile[0]["attack"]} \n'
    result += f' 🛡Физ. защита:{profile[0]["defence"]} \n'
    result += f' 🔰Маг. защита:{profile[0]["defencemagic"]} \n'
    result += f' 🦶Ловкость:{profile[0]["dexterity"]} \n'
    result += f' 🌀Интеллект:{profile[0]["intelligence"]} \n\n'
    result += f' 🌟Очки параметров:{profile[0]["points"]} \n\n'
    print(f'Print profile for {idvk}.')
    return str(result)

def print_mob_profile(idvk):
    #вывод профиля мобв
    profile = select('mob', 'lvl, xp, gold, points, attack, defence, defencemagic, dexterity, intelligence, health', idvk)
    result = f'\n\nХарактеристика моба:\n'
    result += f' 📝Уровень:{profile[0]["lvl"]} \n'
    result += f' 📗Опыт:{profile[0]["xp"]} \n'
    result += f' 🎆Рунная пыль:{profile[0]["gold"]} \n\n'
    result += f' ❤Здоровье:{profile[0]["health"]} \n'
    result += f' 🗡Атака:{profile[0]["attack"]} \n'
    result += f' 🛡Физ. защита:{profile[0]["defence"]} \n'
    result += f' 🔰Маг. защита:{profile[0]["defencemagic"]} \n'
    result += f' 🦶Ловкость:{profile[0]["dexterity"]} \n'
    result += f' 🌀Интеллект:{profile[0]["intelligence"]} \n\n'
    #result += f' 🌟Очки параметров:{profile[0]["points"]} '
    print(f'Print mob for {idvk}.')
    return str(result)

def back(idvk):
    #путь назад
    status = f'Ничего не предвешало беды...'
    return str(status)

def command_attack(idvk):
    #проверка на ловкость
    battle_dexterity_equal(idvk)

def print_battle_turn_player(idvk):
    #конец хода игрока
    player = select('player', 'attack, defence, defencemagic, dexterity, intelligence, health', idvk)
    player_current = select('player_current', 'attack, defence, defencemagic, dexterity, intelligence, health, mana', idvk)
    status = f'\n\nВы:\n'
    status += f' 🗡{player_current[0]["attack"]}/{player[0]["attack"]} 🛡{player_current[0]["defence"]}/{player[0]["defence"]} 🔰{player_current[0]["defencemagic"]}/{player[0]["defencemagic"]}\n'
    status += f'❤{player_current[0]["health"]}/{player[0]["health"]}'
    status += f'⚡{player_current[0]["dexterity"]}/{player[0]["dexterity"]}'
    status += f'🔷{player_current[0]["mana"]}/{player[0]["intelligence"]*2}\n\n'
    print(f'Print battle panel about player for {idvk}')
    return status

def print_battle_turn_mob(idvk):
    #конец хода моба
    player = select('mob', 'attack, defence, defencemagic, dexterity, intelligence, health', idvk)
    player_current = select('mob_current', 'attack, defence, defencemagic, dexterity, intelligence, health, mana', idvk)
    status = f'\n\nМоб: Слизень\n'
    status += f' 🗡{player_current[0]["attack"]}/{player[0]["attack"]} 🛡{player_current[0]["defence"]}/{player[0]["defence"]} 🔰{player_current[0]["defencemagic"]}/{player[0]["defencemagic"]}\n'
    status += f'❤{player_current[0]["health"]}/{player[0]["health"]}'
    status += f'⚡{player_current[0]["dexterity"]}/{player[0]["dexterity"]}'
    status += f'🔷{player_current[0]["mana"]}/{player[0]["intelligence"]*2}\n\n'
    print(f'Print battle panel about mob for {idvk}')
    return status