from modules.sqlite.engine.update import *
from modules.sqlite.engine.add import register
from modules.sqlite.engine.printer import *

def checking(idvk, text):
    config = {
        "профиль": print_profile,
        "начать": register,
        "назад": back,
        "+атк": set_player_attack,
        "+защ":set_player_defence,
        "+лвк":set_player_dexterity,
        "+инт":set_player_intelligence,
        "+здр":set_player_health,
        "сброс": clear_player_points,
        "моб": print_mob_profile
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