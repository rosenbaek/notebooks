import bs4
import requests
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib as mpl
import matplotlib.pyplot as plt
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger') # for POS_tag
nltk.download('maxent_ne_chunker') # for NER
nltk.download('words') # for NER
nltk.download('omw-1.4')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
r = requests.get('https://www.kongehuset.dk/nyheder/laes-h-m-dronningens-nytaarstale-2021')
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'html.parser')

paragraphs = soup.select("body > main > div > main > article > div.rich-text > div > div > p")

paragraphs = [x.text for x in paragraphs]
sentense = ' '.join(paragraphs)

tokens = word_tokenize(sentense)
tokens = list(map(str.lower,tokens))

stop_words = set(stopwords.words('danish'))
tokens = [w for w in tokens if not w in stop_words]
print(tokens)

text = ' '.join(tokens)
# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
mpl.use("pdf")
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('cloud.png',bbox_inches='tight')



