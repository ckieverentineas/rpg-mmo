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
    cursor.execute("""CREATE TABLE IF NOT EXISTS battlepve
    (id INTEGER PRIMARY KEY,
    idvk INTEGER NOT NULL UNIQUE,
    attackplayer INTEGER NOT NULL,
    defenceplayer INTEGER NOT NULL,
    defencemagicplayer INTEGER NOT NULL,
    dexterityplayer INTEGER NOT NULL,
    intelligenceplayer INTEGER NOT NULL,
    healthplayer INTEGER NOT NULL,
    manaplayer INTEGER NOT NULL,
    attackmob INTEGER NOT NULL,
    defencemob INTEGER NOT NULL,
    defencemagicmob INTEGER NOT NULL,
    dexteritymob INTEGER NOT NULL,
    intelligencemob INTEGER NOT NULL,
    healthmob INTEGER NOT NULL,
    manamob INTEGER NOT NULL,
    crdate datetime)
    """)
    cursor.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS rune
    (id INTEGER PRIMARY KEY,
    idvk INTEGER NOT NULL UNIQUE,
    attack INTEGER NOT NULL,
    defence INTEGER NOT NULL,
    defencemagic INTEGER NOT NULL,
    dexterity INTEGER NOT NULL,
    intelligence INTEGER NOT NULL,
    health INTEGER NOT NULL,
    xp INTEGER NOT NULL,
    gold INTEGER NOT NULL,
    loot INTEGER NOT NULL,
    crdate datetime)
    """)
    cursor.commit()
    cursor.close()