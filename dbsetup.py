#-------------------- Set up database
import db
import sqlite3

conn = sqlite3.connect(db.dbname)
c = conn.cursor()
c.execute('''DROP TABLE terms''')
c.execute('''CREATE TABLE if not exists terms
        (english text, url text, category text)''')

import csv

with open('clean-dataset.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    spamreader.__next__() #read header row
    for row in spamreader:
        english = row[2]
        url = row[13]

        t = (english, url, None)
        c.execute("INSERT INTO terms VALUES (?,?,?)", t)

conn.commit()
conn.close()

#-------------------- Adding the categories to the terms --------------------
categories = {
				"numbers": ["TWENTY", "two"],
				"colors": ["red", "blue"]
			}

for category in categories.keys():
	for english in categories[category]:
		db.addCategoryToTerms(category, english)