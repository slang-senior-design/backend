#-------------------- Set up database
import db
import sqlite3

conn = sqlite3.connect(db.dbname)
c = conn.cursor()
c.execute('''DROP TABLE if exists terms''')
c.execute('''CREATE TABLE if not exists terms
        (english text, url text, category text)''')

import csv

with open('clean-dataset.csv', newline='', encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile)
    spamreader.__next__() #read header row
    for row in spamreader:
        english = row[2].lower()
        url = row[13].lower()

        t = (english, url, None)
        c.execute("INSERT INTO terms VALUES (?,?,?)", t)

conn.commit()
conn.close()

#-------------------- Adding the categories to the terms --------------------
import json

with open("vocabulary_terms.json") as f:
	categories = json.loads(f.read())

for category in categories.keys():
	for english in categories[category]:
		db.addCategoryToTerms(category, english)