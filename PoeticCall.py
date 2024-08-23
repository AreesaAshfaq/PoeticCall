import streamlit as st
import openai


def gptPoetry(UserInput):

  response = openai.Completion.create(model="text-davinci-003", prompt=UserInput, max_tokens=1000, temperature = 0.7)
  return response.choices[0]['text']
  
st.markdown("<h1 style='text-align: center; color: black;'> Welcome to Poetic Call</h1>", unsafe_allow_html=True)

st.subject = st.text_input('Subject of Poetry', placeholder=None)
st.language = st.text_input('Language of Poetry', placeholder=None)

st.query = 'genrate' + st.subject + 'poetry in' + st.language 

form = st.form(key='my-form')
submit = form.form_submit_button('Submit')

if submit:
  st.write(gptPoetry(st.query))
st.write(' ')
