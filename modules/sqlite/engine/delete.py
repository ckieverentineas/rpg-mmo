from modules.sqlite.connect import con
from modules.sqlite.engine.select import *
import random

#удаление данных

def delete(table, idvk):
    #Функция удаления данных
    cursor = con()
    sql_delete_query = (f'DELETE from {table} WHERE idvk = {idvk}')
    cursor.execute(sql_delete_query)
    cursor.commit()
    print(f'Deleted record {table} for {idvk}')
    cursor.close()

def delete_item(table, idvk, itemid):
    cursor = con()
    sql_delete_query = (f'DELETE from {table} WHERE idvk = {idvk} and id = {itemid}')
    cursor.execute(sql_delete_query)
    cursor.commit()
    print(f'Deleted item {table} {itemid} for {idvk}')
    cursor.close()