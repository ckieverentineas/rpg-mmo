# Авторизация группы:
import vk_api
import config
from vk_api.longpoll import VkLongPoll, VkEventType
import time
import requests

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

vk_session = vk_api.VkApi(token = config.token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
def get_longpoll():
    try:
        longpoll = VkLongPoll(vk_session)
        for event in longpoll.listen():
            if (event.type == VkEventType.MESSAGE_NEW
                and event.to_me and event.text):
                user_id = event.user_id
                random_id = get_random_id()
                text = event.text
                return vk, user_id, random_id, text
    except vk_api.VkApiError as error_msg:
        print(f'problem char --> {error_msg}')