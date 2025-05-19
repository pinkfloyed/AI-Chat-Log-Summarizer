from utils import extract_keywords
from tfidf_keywords import extract_tfidf_keywords

def generate_summary(user_messages, ai_messages, top_n=5, method="nltk"):
    """
    Generates and prints a summary of a conversation between user and AI.

    Args:
        user_messages (list of str): Messages sent by the user.
        ai_messages (list of str): Messages sent by the AI.
        top_n (int): Number of top keywords to extract (default is 5).
        method (str): Keyword extraction method - "nltk" or "tfidf".

    Prints:
        Summary statistics and main conversation topics with keywords.
    """

    try:
        total_messages = len(user_messages) + len(ai_messages)
        print("\nSummary:")
        print(f"- The conversation had {total_messages} exchanges.")
        print(f"- User messages: {len(user_messages)}")
        print(f"- AI messages: {len(ai_messages)}")

        all_text = " ".join(user_messages + ai_messages)

        if method == "tfidf":
            top_keywords = extract_tfidf_keywords(all_text, top_n=top_n)
        else:
            top_keywords = extract_keywords(all_text, top_n=top_n)

        if top_keywords:
            main_topic_keywords = ', '.join(top_keywords[:4])
            main_topic = f"The conversation was mainly about **{main_topic_keywords}** and related topics."
        else:
            main_topic = "The conversation topic could not be clearly identified."

        print(f"- {main_topic}")
        print(f"- Most common keywords: {', '.join(top_keywords[:5])}")

    except Exception as e:
        print("An error occurred while generating the summary:", str(e))