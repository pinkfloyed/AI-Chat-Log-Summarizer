def parse_chat(file_path):
    user_messages = []
    ai_messages = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.startswith("User:"):
                user_messages.append(line[5:].strip())
            elif line.startswith("AI:"):
                ai_messages.append(line[3:].strip())

    return user_messages, ai_messages
