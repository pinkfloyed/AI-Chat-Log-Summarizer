def parse_chat(file_path):
    """
        Parses a chat log file and separates messages by user and AI.

        Args:
            file_path (str): Path to the chat log text file.

        Returns:
            tuple: A tuple containing two lists:
                - user_messages (list of str): Messages from the user.
                - ai_messages (list of str): Messages from the AI.
        """

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
