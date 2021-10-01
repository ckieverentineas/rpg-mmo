from modules.sqlite.connect import con
#удаление данных

def delete(table, idvk):
    #Функция удаления данных
    cursor = con()
    sql_delete_query = (f'DELETE from {table} WHERE idvk = {idvk}')
    cursor.execute(sql_delete_query)
    cursor.commit()
    print(f'Deleted record {table} for {idvk}')
    cursor.close()