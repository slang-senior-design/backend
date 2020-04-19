import sys
import pathlib
import os
parent = pathlib.Path(__file__).parent.absolute()
root = parent.parent.absolute()
sys.path.append(str(root))
#-------------------- Set up database --------------------
import db
import sqlite3
import convert
import config

dbname = config.dbname

conn = sqlite3.connect(dbname)
c = conn.cursor()
# c.execute('''DROP TABLE if exists terms''')
c.execute('''CREATE TABLE if not exists terms
		(english text, url text, category text)''')

#-------------------- Loads data --------------------
import csv

with open('clean-dataset.csv', newline='', encoding="utf-8") as csvfile:
	spamreader = csv.reader(csvfile)
	next(spamreader) #read header row
	for i in range(0):
		next(spamreader)
	with open("convert_log.txt", "w") as f:
		for i, row in enumerate(spamreader):
			english = row[2].lower()
			url = row[13]
			filename = url.split("/")[-1].split(".")[0]
			url = convert.convert(url, english, f'{filename}.mp4')

			t = (english, url, None)
			c.execute("INSERT INTO terms VALUES (?,?,?)", t)
			f.write(f"Finished: {row[0]}, {english}\n")
			f.flush()
			conn.commit()
conn.close()

#-------------------- Adding the categories to the terms --------------------
import json

with open("vocabulary_terms.json") as f:
	categories = json.loads(f.read())

for category in categories.keys():
	for english in categories[category]:
		db.addCategoryToTerms(category, english)