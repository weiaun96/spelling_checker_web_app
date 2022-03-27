import streamlit as st
from textblob import TextBlob
from spellchecker import SpellChecker
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import re
import collections


st.title('The Spelling Checker')
text = st.text_area("Enter Text: ", value='', height=None, max_chars=None, key=None)


if st.button('Check Spelling'):
    if text == '':
        st.write('No text is entered. Please enter text for checking') 
    else:
        st.write("Original Text:\n", str(text))
        #remove all punctuations before finding possible misspelled words
        s = re.sub(r'[^\w\s]','',text)
        st.write("Text without punctuations:\n",s)
        wordlist=word_tokenize(s)
        spell = SpellChecker()
        # find those words that may be misspelled
        misspelled = list(spell.unknown(wordlist))
        
        corrected = []
        for w in wordlist:
            if w in misspelled:
                correct = spell.correction(w)
                corrected.append(correct)
            else:
                corrected.append(w)
       
        st.write('**The correct spelling is**: ' + str(' '.join(corrected)))
            
else: pass
