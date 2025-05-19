import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from collections import Counter

def extract_keywords(text, top_n=15):
    """
        Extracts the top N keywords and key phrases from the input text.

        Uses unigram filtering and bigram collocation scoring to identify
        significant keywords and phrases, excluding common stopwords.

        Args:
            text (str): The input text to analyze.
            top_n (int): Number of keywords/phrases to return (default 15).

        Returns:
            list: A list of top keywords and bigram phrases sorted by relevance.
    """

    try:
        if not text or not isinstance(text, str):
            raise ValueError("Input text must be a non-empty string.")

        tokens = word_tokenize(text.lower())
        tokens = [t for t in tokens if t.isalpha()]
        stop_words = set(stopwords.words('english'))
        tokens = [t for t in tokens if t not in stop_words]

        bigram_finder = BigramCollocationFinder.from_words(tokens)
        bigrams = bigram_finder.nbest(BigramAssocMeasures.likelihood_ratio, top_n * 3)
        bigram_phrases = [' '.join(bg) for bg in bigrams]

        unigram_counts = Counter(tokens)
        unigrams_filtered = [w for w in unigram_counts if all(w not in phrase.split() for phrase in bigram_phrases)]
        unigrams_sorted = sorted(unigrams_filtered, key=lambda w: unigram_counts[w], reverse=True)

        combined = bigram_phrases + unigrams_sorted
        return combined[:top_n]

    except LookupError as e:
        print("NLTK resource not found. Please ensure 'punkt' and 'stopwords' are downloaded.")
        print("Run: nltk.download('punkt') and nltk.download('stopwords')")
        return []

    except Exception as e:
        print(f"Error extracting keywords: {e}")
        return []
        
