import pandas as pd 
import spacy 


i = 1
while i != 0:
    text1 = input('please enter the text 1')
    text2 = input('please enter the text 2')
    get_score(text1,text2)
    i = int(input('enter 1 to check for a new sentence. to exit enter 0'))

    
    
def get_score(text1,text2):
    nlp = spacy.load('en_core_web_lg')
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    print(doc1.similarity(doc2))
    
