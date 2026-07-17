import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def gptPoetry(subject, language):

    prompt = f"Generate a poem about {subject} in {language}."

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=1000,
        temperature=0.7
    )

    return response.choices[0].message.content


st.markdown(
    "<h1 style='text-align: center; color: black;'>Welcome to Poetic Call</h1>",
    unsafe_allow_html=True
)

subject = st.text_input("Subject of Poetry")
language = st.text_input("Language of Poetry")


form = st.form(key="my-form")
submit = form.form_submit_button("Submit")


if submit:
    poem = gptPoetry(subject, language)
    st.write(poem)

st.write(" ")
