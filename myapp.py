# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 19:26:50 2021

@author: Anoop
"""


import openai
import streamlit as st
def gpt3(stext):
    openai.api_key = '-Your API Key here - Key may vary-'
    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3",
        prompt=stext,
            temperature = 0.1,
            max_tokens = 1000,
            top_p = 1,
            frequency_penalty = 0
    )
    context = response.choices[0].text.split('.')
    print(context)
    return response.choices[0].text

query = "what is the best tech job to make money?"
path = st.text_input("What's your question?")
if path:
    response = gpt3(path)
#print(response)

st.write("Response: " + response)

