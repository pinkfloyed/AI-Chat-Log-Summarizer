from sklearn.feature_extraction.text import TfidfVectorizer

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
        vectorizer = TfidfVectorizer(
            stop_words='english',
            max_features=top_n,
            ngram_range=(1, 2)
        )
        X = vectorizer.fit_transform([text])
        return list(vectorizer.get_feature_names_out())

    except Exception as e:
        print(f"TF-IDF keyword extraction failed: {e}")
        return []

