import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def html_text(link):
	page = requests.get(link)
	soup = BeautifulSoup(page.content, "html.parser")
	title = soup.find(id="question-header").text.strip()
	main = soup.find(id="mainbar").text.strip()
	text = " ".join((title + main).split()) # make text compact
	return text

def preprocess(text):
	# Remove punctuations
	tokenizer = nltk.RegexpTokenizer(r"\w+")
	word_tokens = tokenizer.tokenize(text)

	# Convert to lower case
	word_tokens = [w.lower() for w in word_tokens]

	# Remove stop words
	stop_words = set(stopwords.words('english'))
	word_tokens = [w for w in word_tokens if not w.lower() in stop_words]

	# Remove numbers
	word_tokens = [w for w in word_tokens if not w.isdigit()]

	# Lemmatize
	lemmatizer = WordNetLemmatizer()
	word_tokens = [lemmatizer.lemmatize(w, pos='v') for w in word_tokens] # to lemmatize verb

	return word_tokens
