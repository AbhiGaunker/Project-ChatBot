import nltk
import numpy as np
import json
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

file = open("intents.json")
data = json.load(file)

words = []
label_tag = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

    if intent["tag"] not in label_tag:
        label_tag.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w != "?"]

words = sorted(list(set(words)))
label_tag = sorted(label_tag)








training = []
output = []

out_empty = [0 for _ in range(len(label_tag))]
for x, doc in enumerate(docs_x):
    bag = []

    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[label_tag.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)


training = np.array(training)
output = np.array(output)



