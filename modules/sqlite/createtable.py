import sqlite3
from sqlite3.dbapi2 import Cursor
from modules.sqlite.connect import con
def createdb():
    cursor = con()
    cursor.execute("""CREATE TABLE IF NOT EXISTS player
    (id INTEGER PRIMARY KEY,
    idvk INTEGER NOT NULL UNIQUE,
    lvl INTEGER NOT NULL,
    attack INTEGER NOT NULL,
    defence INTEGER NOT NULL,
    defencemagic INTEGER NOT NULL,
    dexterity INTEGER NOT NULL,
    intelligence INTEGER NOT NULL,
    health INTEGER NOT NULL,
    xp INTEGER NOT NULL,
    gold INTEGER NOT NULL,
    points INTEGER NOT NULL,
    crdate datetime)
    """)
    cursor.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS mob
    (id INTEGER PRIMARY KEY,
    idvk INTEGER NOT NULL UNIQUE,
    lvl INTEGER NOT NULL,
    attack INTEGER NOT NULL,
    defence INTEGER NOT NULL,
    defencemagic INTEGER NOT NULL,
    dexterity INTEGER NOT NULL,
    intelligence INTEGER NOT NULL,
    health INTEGER NOT NULL,
    xp INTEGER NOT NULL,
    gold INTEGER NOT NULL,
    points INTEGER NOT NULL,
    crdate datetime)
    """)
    cursor.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS player_current
    (id INTEGER PRIMARY KEY,
    idvk INTEGER NOT NULL UNIQUE,
    attack INTEGER NOT NULL,
    defence INTEGER NOT NULL,
    defencemagic INTEGER NOT NULL,
    dexterity INTEGER NOT NULL,
    intelligence INTEGER NOT NULL,
    health INTEGER NOT NULL,
    mana INTEGER NOT NULL,
    crdate datetime)
    """)
    cursor.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS mob_current
    (id INTEGER PRIMARY KEY,
    idvk INTEGER NOT NULL UNIQUE,
    attack INTEGER NOT NULL,
    defence INTEGER NOT NULL,
    defencemagic INTEGER NOT NULL,
    dexterity INTEGER NOT NULL,
    intelligence INTEGER NOT NULL,
    health INTEGER NOT NULL,
    mana INTEGER NOT NULL,
    crdate datetime)
    """)
    cursor.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS rune
    (id INTEGER PRIMARY KEY,
    idvk INTEGER NOT NULL,
    lvl INTEGER NOT NULL,
    attack INTEGER NOT NULL,
    defence INTEGER NOT NULL,
    defencemagic INTEGER NOT NULL,
    dexterity INTEGER NOT NULL,
    intelligence INTEGER NOT NULL,
    health INTEGER NOT NULL,
    xp INTEGER NOT NULL,
    gold INTEGER NOT NULL,
    loot INTEGER NOT NULL,
    equip INTEGER NOT NULL,
    crdate datetime)
    """)
    cursor.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS setting
    (id INTEGER PRIMARY KEY,
    idvk INTEGER NOT NULL UNIQUE,
    lvl INTEGER NOT NULL,
    costattack INTEGER NOT NULL,
    itemid INTEGER NOT NULL,
    crdate datetime)
    """)
    cursor.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS reward
    (id INTEGER PRIMARY KEY,
    idvk INTEGER NOT NULL UNIQUE,
    xp INTEGER NOT NULL,
    gold INTEGER NOT NULL,
    crdate datetime)
    """)
    cursor.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS inventory
    (id INTEGER PRIMARY KEY,
    idvk INTEGER NOT NULL,
    mythical INTEGER NOT NULL,
    legendary INTEGER NOT NULL,
    epic INTEGER NOT NULL,
    rare INTEGER NOT NULL,
    unusual INTEGER NOT NULL,
    usual INTEGER NOT NULL,
    water INTEGER NOT NULL,
    runic INTEGER NOT NULL,
    flower INTEGER NOT NULL,
    potionlife INTEGER NOT NULL,
    potionmana INTEGER NOT NULL,
    crdate datetime)
    """)
    cursor.commit()
    cursor.close()