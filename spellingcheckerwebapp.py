import streamlit as st
from textblob import TextBlob

st.title('The Spelling Checker')
text = st.text_area("Enter Text: ", value='', height=None, max_chars=None, key=None)

if st.button('Check Spelling'):
    if text == '':
        st.write('No text is entered. Please enter text for checking') 
    else: 
        result = TextBlob(text)
        st.write('**The correct spelling is**: ' + str(result.correct()))
else: pass