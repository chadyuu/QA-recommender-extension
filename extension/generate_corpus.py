import sqlite3
import gensim
import pickle
import common

# nltk.download('all')

sqliteConnection = sqlite3.connect('tis.db')
cursor = sqliteConnection.cursor()
cursor.execute('SELECT id, text FROM questions where text IS NOT NULL')
links = cursor.fetchall()
docs = []
ids = []

for link in links:
	id = link[0]
	text = link[1]
	word_tokens = common.preprocess(text)
	docs.append(word_tokens)
	ids.append(id)

dictionary = gensim.corpora.Dictionary(docs)
corpus = [dictionary.doc2bow(doc) for doc in docs]
with open('dictionary', 'wb') as dictionary_file:
  pickle.dump(dictionary, dictionary_file)
with open('corpus', 'wb') as corpus_file:
  pickle.dump(corpus, corpus_file)
with open('ids', 'wb') as ids_file:
  pickle.dump(ids, ids_file)