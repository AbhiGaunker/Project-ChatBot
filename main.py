import random
import numpy as np
import datetime
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()



from preprocessData import label_tag ,data
from Mmodel import bag_of_words ,create_model
from webscraping import web_scraping


model = create_model()
model.load('model.tflearn')


def response(inp):
    if inp[:3] == "***":
        return "didn't catch what you said can you repeat or else you can type it"

    results = model.predict([bag_of_words(inp)])
    results_index = np.argmax(results)
    tag = label_tag[results_index]


    for tg in data["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']
    if random.choice(responses) == "webscraping":
        return web_scraping(inp)
    return random.choice(responses)



def wishme():
    hour = datetime.datetime.now().hour
    date = datetime.date.today()
    if 0 <= hour < 12:
        text = f"Good Morning sir. Welcome to VIT bhopal chatbot                     date:  {date}"
    elif 12 <= hour < 18:
        text = f"Good Afternoon sir. Welcome to VIT bhopal chatbot                   date:  {date}"
    else:
        text = f"Good Evening sir. Welcome to VIT bhopal chatbot                     date:  {date}"

    return text




