import sqlite3
import common

sqliteConnection = sqlite3.connect('tis.db')
cursor = sqliteConnection.cursor()
cursor.execute('SELECT id, link FROM questions where text IS NULL')
links = cursor.fetchall()

for link in links:
	id = link[0]
	link = link[1]
	text = common.html_text(link)

	cursor.execute("UPDATE questions SET text = ? where id = ?", (text, id))
	sqliteConnection.commit()
	print(id)

cursor.close()
sqliteConnection.close()