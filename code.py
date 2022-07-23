import pandas as pd 
import spacy 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

i = 1
while i != '0':
    text1 = input('please enter the text 1')
    text2 = input('please enter the text 2')
    get_score(text1,text2)
    i = input('enter 1 to check for a new sentence. to exit enter 0')
    
    
def get_score(text1,text2):
    nlp = spacy.load('en_core_web_lg')
    lemma1 = clean(text1)
    lemma2 = clean(text2)
    doc1 = nlp(lemma1)
    doc2 = nlp(lemma2)
    print(doc1.similarity(doc2))
  


def clean(text):
    token = [token for token in word_tokenize(text) if token not in stopwords.words('english')]
    lemma = lemmatizer.lemmatize(' '.join(token))
    return ' '.join(lemma)
