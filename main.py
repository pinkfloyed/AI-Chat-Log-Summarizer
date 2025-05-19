from chat_parser import parse_chat
from utils import extract_keywords
from summary_generator import generate_summary


def main():
    """
    Main script to parse chat logs and generate a summary.

    - Reads chat data from a file.
    - Extracts user and AI messages.
    - Generates a summary of the conversation.
    """

    chat_file = "data/chat.txt"

    try:
        # Prompt the user to choose method
        method = input("Choose keyword extraction method (nltk / tfidf): ").strip().lower()
        if method not in ["nltk", "tfidf"]:
            print("Invalid method selected. Defaulting to 'nltk'.")
            method = "nltk"

        user_msgs, ai_msgs = parse_chat(chat_file)
        generate_summary(user_msgs, ai_msgs, top_n=5, method=method)

    except FileNotFoundError:
        print(f"Error: Chat file not found at '{chat_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
