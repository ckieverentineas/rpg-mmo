from logging import error
from modules.enter import get_longpoll
import vk_api
from modules import sent
from modules.sqlite.controldb import crdb
from modules.control import checking
def main():
    crdb()
    print("Bot started")
    while True:
        try:  
            while True:
                #longpoll
                vk, ida, idrand, text = get_longpoll()
                #генерация ответа пользователю
                res, sending = checking(ida, text)
                #отправка ответа пользователю
                if (sending == True):
                    print("Sent...")
                    sent(vk, ida, idrand, res, text)
        except vk_api.VkApiError as error_msg:
            print(f'problem char --> {error_msg}')
main()
