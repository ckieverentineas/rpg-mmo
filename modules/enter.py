# Авторизация группы:
import vk_api
import config
from vk_api.longpoll import VkLongPoll, VkEventType
import time
import requests

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from modules.control.control import checking
from modules.sent import sent

vk_session = vk_api.VkApi(token = config.token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

async def get_longpoll():
    print(f'Longpool')
    try:
        try:
            longpoll = VkLongPoll(vk_session)
            for event in longpoll.listen():
                if (event.type == VkEventType.MESSAGE_NEW
                    and event.to_me and event.text):
                    user_id = event.user_id
                    random_id = get_random_id()
                    text = event.text
                    res, sending = await checking(user_id, text)
                    #отправка ответа пользователю
                    if (sending == True):
                        await sent(vk, user_id, random_id, res, text)
        except requests.exceptions.RequestException as error_msg:
            print(f'problem char --> {error_msg}') 
    except vk_api.VkApiError as error_msg:
        print(f'problem char --> {error_msg}')