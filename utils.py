import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from collections import Counter

def extract_keywords(text, top_n=15):
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t.isalpha()]
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t not in stop_words]

    bigram_finder = BigramCollocationFinder.from_words(tokens)
    bigrams = bigram_finder.nbest(BigramAssocMeasures.likelihood_ratio, top_n * 3)
    bigram_phrases = [' '.join(bg) for bg in bigrams]

    unigram_counts = Counter(tokens)
    unigrams_filtered = [w for w in unigram_counts if all(w not in phrase.split() for phrase in bigram_phrases)]

    combined = bigram_phrases + unigrams_filtered
    return combined[:top_n]

