from chat_parser import parse_chat

def main():
    chat_file = "data/chat.txt"
    user_msgs, ai_msgs = parse_chat(chat_file)

if __name__ == "__main__":
    main()
