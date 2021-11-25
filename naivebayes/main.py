from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
#from nltk.cluster import KMeansClusterer, euclidean_distance
#from gensim import corpora, models, utils
#from numpy import array

document = open("matrix.txt", "r")
documents = []
with open('matrix.txt','r') as f:
    for line in f:
        for word in line.split():
           #print(word)
           documents.append(word)
#removing whitespaces, punctuations, stopwords, and stemming words
for document in documents:
    tokenizer = RegexpTokenizer(r'\w+')
    intermediate = tokenizer.tokenize(document)
    stop = stopwords.words('english')
    intermediate = [i for i in intermediate if i not in stop]
    # FIXME: using other stemmers also to know quality of each stemmed text
    lanste = LancasterStemmer()
    intermediate = [lanste.stem(i) for i in intermediate]
    processed.append(intermediate)