from chat_parser import parse_chat
from utils import extract_keywords
from summary_generator import generate_summary


def main():
    chat_file = "data/chat.txt"
    user_msgs, ai_msgs = parse_chat(chat_file)
    generate_summary(user_msgs, ai_msgs, top_n=10)

if __name__ == "__main__":
    main()
