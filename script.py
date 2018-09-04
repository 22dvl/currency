import json, requests, urllib
import sqlite3
import time

n = 60  # Повторение скрипта раз в n секунд
while True:
    db = "new.db"  # название БД в папке со скриптом
    db = sqlite3.connect(db)
    c = db.cursor()
    with urllib.request.urlopen("https://api.exmo.com/v1/ticker/") as url: # Путь к json
        j = json.loads(url.read().decode())
        for row in j:
            buy_price = str(j[row]['buy_price'])
            sell_price = str(j[row]['sell_price'])
            last_trade = str(j[row]['last_trade'])
            high = str(j[row]['high'])
            low = str(j[row]['low'])
            avg = str(j[row]['avg'])
            vol = str(j[row]['vol'])
            vol_curr = str(j[row]['vol_curr'])
            updated = str(j[row]['updated'])
            try:
                c.execute("INSERT INTO " + row + " VALUES (" + updated + "," + buy_price + "," + sell_price + "," +
                          last_trade + "," + high + "," + low + "," + avg + "," + vol + "," + vol_curr + ")")
            except sqlite3.OperationalError:
                c.execute('''CREATE TABLE ''' + row + '''
                            (updated integer, buy_price real, sell_price real, last_trade real, high real, low real, 
                             _avg real, vol real, vol_curr real)''')
                c.execute("INSERT INTO " + row + " VALUES (" + updated + "," + buy_price + "," + sell_price + "," +
                          last_trade + "," + high + "," + low + "," + avg + "," + vol + "," + vol_curr + ")")
    db.commit()
    db.close()
    time.sleep(n)
