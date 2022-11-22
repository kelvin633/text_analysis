from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#Importing the StringIO module.
from io import StringIO 
import glob, nltk, os, re
from nltk.corpus import stopwords
nltk.download('punkt')
import nltk
nltk.download('stopwords')
import altair as alt



st.set_page_config(layout='wide')
st.write('## Analyzing Shakespeare Texts')

# Sidebar 
st.sidebar.header("Word Cloud Settings")
max_word = st.sidebar.slider("Max Words", 10,200,100,10)
max_font = st.sidebar.slider("Size of largest words", 50,350,60)
image_size = st.sidebar.slider("Image width", 100,800,400,10)
random = st.sidebar.slider("Random State", 30,100,42)
remove = st.sidebar.checkbox( "Remove Stop Words?")


st.sidebar.header("Word Count Settings")
min_word = st.sidebar.slider("Minimum Count of Words", 5,100,100,1)

# Creating a dictionary not a list 
books = {" ":" ","A Mid Summer Night's Dream":"data/summer.txt",
"The Merchant of Venice":"data/merchant.txt","Romeo and Juliet":"data/romeo.txt"}
## Select text files
image = st.selectbox("Choose a txt file", books.keys())
image = books.get(image)


# OLD CODE 
#image  = st.selectbox(' Choose a text file', (' ', 'A Mid Summer Nights Dream', 'The Merchant of Venice', 'Romeo and Juliet'))
#st.write('You selected:', option)
#fp = st.sidebar.file_uploader("hello") 
#image = st.file_uploader("Choose a txt file")


#Tokenize the dataset 
#tokens = nltk.word_tokenize(dataset)
#tokens = [w for w in tokens if not w.lower() in stopwords]
#filtered_text = [w for w in tokens if not w.lower() in stopwords]
#frequency = nltk.FreqDist(tokens)
#freq_df = pd.DataFrame(frequency.items(),columns=['word','count'])


#if selection is not None: 
if image != " ":
  stopwords = []
  raw_text = open(image,"r").read().lower()
  #nltk_stop_words = stopwords.words('english')
  dataset = re.sub(r'[^\w\s]','',raw_text)
  # To convert to a string based IO:
  #stringio = StringIO(image.getvalue().decode("utf-8"))
  #st.write(stringio)
  # To read file as string:
  #dataset = stringio.read()
  #st.write(dataset)

  #Tokenize the dataset 
#tokens = nltk.word_tokenize(dataset)
#tokens = [w for w in tokens if not w.lower() in stopwords]
#filtered_text = [w for w in tokens if not w.lower() in stopwords]
#frequency = nltk.FreqDist(tokens)
#freq_df = pd.DataFrame(frequency.items(),columns=['word','count'])

  stopwords = set(STOPWORDS)
  stopwords.update(['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may',
    'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
    'put', 'seem', 'asked', 'made', 'half', 'much',
    'certainly', 'might', 'came'])

tab1,tab2,tab3 = st.tabs(['WordCloud','Bar Chart','View Text'])

#Tokenize the dataset 
#tokens = nltk.word_tokenize(dataset)
#tokens = [w for w in tokens if not w.lower() in stopwords]
#filtered_text = [w for w in tokens if not w.lower() in stopwords]
#frequency = nltk.FreqDist(tokens)
#freq_df = pd.DataFrame(frequency.items(),columns=['word','count'])



with tab1:

    if  image != " ":
        cloud = WordCloud(background_color = "white", 
                            max_words = max_word, 
                            max_font_size=max_font, 
                            stopwords = stopwords, 
                            random_state=random)
        #wc = cloud.generate(raw_text)
        wc = cloud.generate(dataset)
        word_cloud = cloud.to_file('wordcloud.png')
        st.image(wc.to_array() ,width=image_size)
   




with tab2:
    if image != " ":
        st.write('Put your bar chart here')

with tab3:
    if image != " ":
       st.write(raw_text)