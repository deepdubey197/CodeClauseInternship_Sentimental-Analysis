from textblob import TextBlob
import streamlit as st
st.title("Sentimental Analysis")
text=st.text_area("Enter text to analyze it's nature ")
blob=TextBlob(text)
if st.button("Analyze"):
    sentiment = blob.sentiment.polarity
    if sentiment < 0:
        st.header("Negative Statement")
        st.write(sentiment)
    if sentiment > 0:
        st.header("Positive Statement")
        st.write(sentiment)
    if sentiment >= 0 and sentiment <= 0.2:
        st.header("Neutral Statement")
        st.write(sentiment)

