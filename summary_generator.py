from utils import extract_keywords
from tfidf_keywords import extract_tfidf_keywords

def generate_summary(user_messages, ai_messages, top_n=5, method="nltk", return_lines=False):
    """
    Generates a summary of a conversation between user and AI.

    Args:
        user_messages (list of str)
        ai_messages (list of str)
        top_n (int)
        method (str): "nltk" or "tfidf"
        return_lines (bool): If True, return summary as list of strings instead of printing

    Returns:
        list or None: Returns summary lines if return_lines=True, else prints summary.
    """

    try:
        total_messages = len(user_messages) + len(ai_messages)
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

        summary_lines = [
            "\nSummary:",
            f"- The conversation had {total_messages} exchanges.",
            f"- User messages: {len(user_messages)}",
            f"- AI messages: {len(ai_messages)}",
            f"- {main_topic}",
            f"- Most common keywords: {', '.join(top_keywords[:5])}"
        ]

        if return_lines:
            return summary_lines
        else:
            for line in summary_lines:
                print(line)

    except Exception as e:
        error_msg = f"An error occurred while generating the summary: {e}"
        if return_lines:
            return [error_msg]
        else:
            print(error_msg)
