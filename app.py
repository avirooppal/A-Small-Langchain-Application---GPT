import os 
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI


os.environ['OPENAI_API_KEY'] = apikey

st.title('Just A Rather 🦜🔗 Application - A GPT ')
prompt = st.text_input('Enter Prompt')

llm = OpenAI(temperature=0.9)

if prompt:
    response = llm(prompt)
    st.write(response)