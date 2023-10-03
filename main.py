import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from pathlib import Path
import glob
import plotly.express as px


analyzer = SentimentIntensityAnalyzer()
neg = []
pos = []

filepaths = glob.glob("diary/*.txt")
for filepath in sorted(filepaths):
    with open(filepath)as file:
        content = file.read()
    score = analyzer.polarity_scores(content)
    neg.append(score['neg'])
    pos.append(score['pos'])

date = []
for filedate in filepaths:
    date.append(Path(filedate).stem)

# date = [name.strip(".txt").strip("diary\\") for name in filepaths]

st.title("Diary Tone")
st.subheader("Positivity")
pos_figure = px.line(x=date, y=pos, labels={"x": "Date", "y": "Positive"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=date, y=neg, labels={"x": "Date", "y": "Negative"})
st.plotly_chart(neg_figure)