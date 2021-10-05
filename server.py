from logging import error
from modules.enter import get_longpoll
import vk_api
from modules.sqlite.controldb import crdb
import asyncio
async def main():
    crdb()
    print("Bot started")
    while True:
        try:  
            while True:
                #longpoll
                await get_longpoll()
                #генерация ответа пользователю
        except vk_api.VkApiError as error_msg:
            print(f'problem char --> {error_msg}')
asyncio.run(main())
