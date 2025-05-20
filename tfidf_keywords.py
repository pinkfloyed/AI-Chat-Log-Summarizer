from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def extract_tfidf_keywords(text, top_n=10):
    """
    Extracts top keywords using TF-IDF (unigrams + bigrams).

    Args:
        text (str): Input chat log text.
        top_n (int): Number of keywords to return.

    Returns:
        list: Top TF-IDF keywords/phrases.
    """

    try:
        if not text or not text.strip():
            raise ValueError("Empty or invalid input text.")

        vectorizer = TfidfVectorizer(
            stop_words='english',
            ngram_range=(1, 2)
        )
        X = vectorizer.fit_transform([text])
        feature_array = np.array(vectorizer.get_feature_names_out())
        tfidf_scores = X.toarray()[0]
        top_indices = tfidf_scores.argsort()[::-1][:top_n]
        top_keywords = feature_array[top_indices]

        return top_keywords.tolist()

    except Exception as e:
        print(f"TF-IDF keyword extraction failed: {e}")
        return []

