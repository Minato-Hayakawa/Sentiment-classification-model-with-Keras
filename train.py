import pandas as pd
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences
FilePath='C:/vscode/python/Twitter US Airline Sentiment/Tweets.csv/Tweets.csv'

df=pd.read_csv(FilePath)
text=df['text'].values
labels=df['airline_sentiment'].map('positive':0,'neutral':1,'nagetive':2,)