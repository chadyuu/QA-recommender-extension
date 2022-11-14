from flask import Flask, request
import gensim
from nltk.tokenize import word_tokenize
import pickle
import numpy as np
import common

app = Flask(__name__)

@app.route('/get')
def index():
  link = request.args.get('link', default = '', type = str)

  with open('dictionary', 'rb') as dictionary_file:
    dictionary = pickle.load(dictionary_file)
  with open('corpus', 'rb') as corpus_file:
    corpus = pickle.load(corpus_file)
  with open('ids', 'rb') as ids_file:
    ids = pickle.load(ids_file)

  tf_idf = gensim.models.TfidfModel(corpus)
  sims = gensim.similarities.Similarity('workdir/', tf_idf[corpus], num_features=len(dictionary))  # calculate cosine similarity

  text = common.html_text(link)
  query_doc = [w.lower() for w in word_tokenize(text)]
  query_doc_bow = dictionary.doc2bow(query_doc)
  query_doc_tf_idf = tf_idf[query_doc_bow]

  # return the 4 most similar document index
  top_idx = np.argsort(-sims[query_doc_tf_idf])[0:4]
  top_ids = [ids[i] for i in top_idx]
  return top_ids

if __name__ == "__main__":
  app.run(debug=True)
