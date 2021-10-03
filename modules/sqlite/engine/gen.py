#Генерация и инициализации
from modules.sqlite.engine.add import generate_battle, generate_mob
from modules.sqlite.engine.delete import *
from modules.sqlite.engine.printer import print_battle_turn_mob, print_battle_turn_player, print_mob_profile, print_profile
from modules.sqlite.engine.update import *


def reseach(idvk):
    delete('mob_current',idvk)
    delete('player_current',idvk)
    delete('mob',idvk)
    generate_mob(idvk)
    generate_battle(idvk)
    costattack = battle_dexterity_equal(idvk)
    update('setting', 'costattack', costattack, idvk)
    status = print_mob_profile(idvk)
    return status