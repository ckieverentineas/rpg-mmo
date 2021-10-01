from modules.sqlite.engine.add import generate_mob
from modules.sqlite.engine.select import *
#Выводы данных из баз данных
def print_profile(idvk):
    #вывод профиля
    profile = select('player', 'lvl, xp, gold, points, attack, defence, dexterity, intelligence, health', idvk)
    result = f' 📝Уровень:{profile[0]["lvl"]} \n'
    result += f' 📗Опыт:{profile[0]["xp"]} \n'
    result += f' 🎆Рунная пыль:{profile[0]["gold"]} \n\n'
    result += f' 🗡Атака:{profile[0]["attack"]} \n'
    result += f' 🛡Защита:{profile[0]["defence"]} \n'
    result += f' 🦶Ловкость:{profile[0]["dexterity"]} \n'
    result += f' 🌀Интеллект:{profile[0]["intelligence"]} \n'
    result += f' ❤Здоровье:{profile[0]["health"]} \n\n'
    result += f' 🌟Очки параметров:{profile[0]["points"]} '
    return str(result)

def print_mob_profile(idvk):
    #вывод профиля мобв
    generate_mob(idvk)
    profile = select('mob', 'lvl, xp, gold, points, attack, defence, dexterity, intelligence, health', idvk)
    result = f' 📝Уровень:{profile[0]["lvl"]} \n'
    result += f' 📗Опыт:{profile[0]["xp"]} \n'
    result += f' 🎆Рунная пыль:{profile[0]["gold"]} \n\n'
    result += f' 🗡Атака:{profile[0]["attack"]} \n'
    result += f' 🛡Защита:{profile[0]["defence"]} \n'
    result += f' 🦶Ловкость:{profile[0]["dexterity"]} \n'
    result += f' 🌀Интеллект:{profile[0]["intelligence"]} \n'
    result += f' ❤Здоровье:{profile[0]["health"]} \n\n'
    #result += f' 🌟Очки параметров:{profile[0]["points"]} '
    return str(result)

def back(idvk):
    #путь назад
    status = f'Ничего не предвешало беды...'
    return str(status)
    