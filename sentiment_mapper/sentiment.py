from textblob import TextBlob


def analyze_sentiment(text):
    blob = TextBlob(text)
    sentences = blob.sentences
    analysis = [{'text': str(sentence),
                 'polarity': sentence.sentiment.polarity,
                 'subjectivity': sentence.sentiment.subjectivity}
                for sentence in sentences]
    return analysis
