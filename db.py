import os
import sqlite3

if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }

db = "slang.db"

def createTable():
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('''CREATE TABLE if not exists stocks
             (date text, trans text, symbol text, qty real, price real)''')
    conn.commit()
    conn.close()

def insertTable():
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    conn.commit()
    conn.close()

def selectTable():
    conn = sqlite3.connect(db)
    c = conn.cursor()
    t = ('RHAT',)
    c.execute('SELECT * FROM stocks WHERE symbol=?', t)
    e = c.fetchone()
    conn.commit()
    conn.close()
    return e