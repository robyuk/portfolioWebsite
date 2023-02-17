import streamlit as st
import pandas
from pathlib import Path

imageDir = 'images/'
df = pandas.read_csv('data.csv', sep=',')

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image(imageDir + 'photo.png')

with col2:
    st.title('Robert Young')
    content = """
    Hi! I'm Robert and I am an IT Consultant specialising in automation. 
    I have many years experience in gathering requirements and use cases, 
    through delivering complete hardware and software solutions.
    """
    st.write(content)

content = 'Below you can find some of the apps I have written in Python.  ' \
          'You can contact me via the contact page'
st.write(content)

col1, mtCol, col2 = st.columns([2, 0.5, 2])

with col1:
    for index, row in df[:10].iterrows():
        st.title(row['title'])
        imagePath = str(Path('images', row['image']))
        st.image(imagePath)
        st.write(row['description'])
        st.write(f"[Source Code]({row['url']})")


with col2:
    for index, row in df[10:].iterrows():
        st.title(row["title"])
        imagePath = str(Path('images', row['image']))
        st.image(imagePath)
        st.write(row['description'])
        st.write(f"[Source Code]({row['url']})")
