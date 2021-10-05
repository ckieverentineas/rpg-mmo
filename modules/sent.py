import vk_api
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from modules.sqlite.engine import keyboards
from modules.sqlite.engine.update import player_dead, player_win

async def sent(vk, user_id, get_randid, mes, text):
    #запуск события печати
    vk.messages.setActivity(type='typing', peer_id = int(user_id))
    keyboard = keyboards(text)
    try:
        if (keyboard != False):
            vk.messages.send(
                keyboard= keyboard.get_keyboard(),
                user_id = user_id,
                random_id = get_randid,
                message = str(mes)
            )
        else:
            vk.messages.send(
                user_id = user_id,
                random_id = get_randid,
                message = str(mes)
            )
    except vk_api.VkApiError as error_msg:
        print(f'problem char --> {error_msg}')