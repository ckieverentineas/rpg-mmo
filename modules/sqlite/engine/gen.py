#Генерация и инициализации
from modules.sqlite.engine.add import generate_battle, generate_mob
from modules.sqlite.engine.delete import delete
from modules.sqlite.engine.printer import print_mob_profile
from modules.sqlite.engine.select import select
from modules.sqlite.engine.update import update, use_runes_equip, battle_dexterity_equal


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