import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def sentiment_analyzer(text):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    if scores['compound'] >= 0.5:
        return 'POSITIVE'
    elif scores['compound'] <= -0.5:
        return 'NEGATIVE'
    else:
        return 'NEUTRAL'

def score_text(text):
    sid = SentimentIntensityAnalyzer()
    value = sid.polarity_scores(text)
    return value['compound']


