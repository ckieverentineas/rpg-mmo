from modules.sqlite.engine.update import clear_player_points, set_player_attack, set_player_defmagic, set_player_defphysical, set_player_dexterity, set_player_health, set_player_intelligence
from modules.sqlite.engine.add import register
from modules.sqlite.engine.printer import *

def checking(idvk, text):
    config = {
        "профиль": print_profile,
        "моб": mob_profile,
        "начать": register,
        "назад": back,
        "+атк": set_player_attack,
        "+мзащ":set_player_defmagic,
        "+фзащ":set_player_defphysical,
        "+лвк":set_player_dexterity,
        "+инт":set_player_intelligence,
        "+здр":set_player_health,
        "сброс": clear_player_points
    }
    try:
        text = text.lower()
        if (be(idvk) == True or text == "начать"):
            status = config[text](idvk)
            return str(status), True
        else:
            status = f'Напишите: Начать\n Чтобы инициализировать аккаунт.'
            return status, True
    except KeyError as e:
        print(f'Not found action for {e}')
        return '', False