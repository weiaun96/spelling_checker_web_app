import streamlit as st
from spellchecker import SpellChecker

st.title('The Spelling Checker')
text = st.text_area("Enter Text: ", value='', height=None, max_chars=None, key=None)

if st.button('Check Spelling'):
    if text == '':
        st.write('No text is entered. Please enter text for checking') 
    else:
        spell = SpellChecker()
        misspelled = spell.unknown(text)
        for word in misspelled:
            st.write('**The correct spelling is**: ' + str(spell.correction(text)))
            break
else: pass
