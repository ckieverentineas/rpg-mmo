from modules.sqlite.engine.gen import reseach
from modules.sqlite.engine.update import *
from modules.sqlite.engine.add import register
from modules.sqlite.engine.printer import *
import re

async def checking(idvk, text):
    config = {
        "профиль": print_profile,
        "начать": register,
        "назад": back,
        "+атк": set_player_attack,
        "+фзащ":set_player_defence,
        "+мзащ":set_player_defencemagic,
        "+лвк":set_player_dexterity,
        "+инт":set_player_intelligence,
        "+здр":set_player_health,
        "сброс": clear_player_points,
        "исследовать": reseach,
        "атака": battle_control,
        "+ур": lvl_next,
        "-ур": lvl_down,
        "wipe": reward,
        "руна": print_rune,
        "надеть": rune_equip,
        "снять": rune_unequip,
        "сломать": rune_delete,
        "+руна": rune_next,
        "-руна": rune_down,
    }
    try:
        text = text.lower()
        if (be(idvk) == True or text == "начать"):
            status = config[re.sub('\d', '', text)](idvk)
            return str(status), True
        else:
            status = f'Напишите: Начать\n Чтобы инициализировать аккаунт.'
            return status, True
    except KeyError as e:
        print(f'Not found action for {e}')
        return '', False