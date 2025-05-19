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
    user_msgs, ai_msgs = parse_chat(chat_file)
    generate_summary(user_msgs, ai_msgs, top_n=10)

if __name__ == "__main__":
    main()
