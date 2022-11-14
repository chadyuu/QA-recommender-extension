from stackapi import StackAPI
import sqlite3

sqliteConnection = sqlite3.connect('tis.db')

SITE = StackAPI('stackoverflow')
SITE.page_size = 100 # 100 is maximum; returns 500 questions

keywords = [
	 "text mining"
	,"text retrieval"
	,"text information"
	,"natural language processing"
	,"BM25"
	,"POS tagging"
	,"pivoted length normalization"
	,"document frequence"
	,"term frequence"
	,"query likelihood"
	,"PL2"
	,"vector support machine"
	,"TF-IDF"
	,"inverse document frequency"
	,"okapi"
	,"search engine"
	,"zipf's law"
	,"f-measure"
	,"normalized discounted culumative gain"
	,"unigram"
	,"dirichlet prior smoothing"
	,"Jelinek-Mercer"
	,"Rocchio Feedback"
	,"Kullback-Leibler"
	,"pagerank"
	,"hypertext induced topic search"
	,"content based filtering"
	,"beta-gamma threshold learning"
	,"collaborative filtering"
]

inserts = []
for keyword in keywords:
	questions = SITE.fetch('search/advanced', q=keyword, sort="votes")
	for question in questions["items"]:
		inserts.append((question["question_id"], question["link"]))

cursor = sqliteConnection.cursor()
cursor.executemany('INSERT OR IGNORE INTO questions (id, link) values(?, ?)', inserts)
sqliteConnection.commit()
cursor.close()
sqliteConnection.close()