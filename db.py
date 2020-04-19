import os
import sqlite3
import config

dbname = config.dbname

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

def getTerm(english):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    t = (english,)
    c.execute('SELECT * from terms where english=?', t)
    e = c.fetchall()
    conn.commit()
    conn.close()
    return e

def getCategories():
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('SELECT DISTINCT category from terms where category is not null')
    e = c.fetchall()
    flat_list = [item for sublist in e for item in sublist]
    conn.commit()
    conn.close()
    return flat_list