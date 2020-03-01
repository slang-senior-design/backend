import os
import sqlite3

#-------------------- This is for MySQL, which we aren't using but may later look into
# if 'RDS_HOSTNAME' in os.environ:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': os.environ['RDS_DB_NAME'],
#             'USER': os.environ['RDS_USERNAME'],
#             'PASSWORD': os.environ['RDS_PASSWORD'],
#             'HOST': os.environ['RDS_HOSTNAME'],
#             'PORT': os.environ['RDS_PORT'],
#         }
#     }
#--------------------

dbname = "slang.db" # for local testing

def createTable():
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('''CREATE TABLE if not exists stocks
             (date text, trans text, symbol text, qty real, price real)''')
    conn.commit()
    conn.close()

def insertTerms(english, url):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    t = (english, url)
    c.execute("INSERT INTO terms VALUES (?,?)", t)
    conn.commit()
    conn.close()

def getAllTerms():
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('SELECT * from terms')
    e = c.fetchall()
    conn.commit()
    conn.close()
    return e

def addCategoryToTerms(category, english):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('UPDATE terms SET category=? where english=?', (category, english))
    conn.commit()
    conn.close()

def getTermsByCategory(category):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    t = (category,)
    c.execute('SELECT * from terms where category=?', t)
    e = c.fetchall()
    conn.commit()
    conn.close()
    return e

def getCategories():
    return ['fruits', 'and shit']