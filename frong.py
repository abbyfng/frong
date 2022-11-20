from os import terminal_size
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import neattext.functions as nfx

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline

def learn():
    data = pd.read_csv("dataset.csv")
    data.head()
    data['Emotion'].value_counts()

    data['Clean_Text'] = data['Text'].apply(nfx.remove_userhandles)
    data['Clean_Text'] = data['Text'].apply(nfx.remove_stopwords)

    x = data['Clean_Text']
    y = data['Emotion']

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)
    pipe_lr = Pipeline(steps=[('cv',CountVectorizer()),('lr',LogisticRegression())])
    pipe_lr.fit(x_train, y_train)
    #accuracy score
    pipe_lr.score(x_test, y_test)
    return pipe_lr

def emotionToInteger(emotion):
    if (emotion == 'sadness' or emotion == 'shame' ) :
        return 1
    elif (emotion == 'fear'):
        return 2
    elif (emotion == 'anger' or emotion == 'disgust' ):
        return 3
    elif (emotion == 'neutral'):
        return 4
    elif (emotion == 'surprise'):
        return 5
    elif (emotion == 'joy'):
        return 6       
    
def main(sentence):
    pipe = learn()
    emotion = pipe.predict([sentence])
    print(emotion)
    return emotionToInteger(emotion)


#sentence = input("\nhow are u feeling: ")
# sentence = input("\nhow are u feeling: ")
# while (sentence != 'quit'):
#     pipe = learn()
#     emotion = pipe.predict([sentence])
#     print(emotion)
#     print(emotionToInteger(emotion))
#     sentence = input("\nhow are u feeling: ")
