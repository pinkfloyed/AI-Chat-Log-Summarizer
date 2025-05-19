from utils import extract_keywords

def generate_summary(user_messages, ai_messages, top_n=10):
    total_messages = len(user_messages) + len(ai_messages)
    print("\nSummary:")
    print(f"- The conversation had {total_messages} exchanges.")
    print(f"- User messages: {len(user_messages)}")
    print(f"- AI messages: {len(ai_messages)}")

    all_text = " ".join(user_messages + ai_messages)
    top_keywords = extract_keywords(all_text, top_n=top_n)

    if top_keywords:
        main_topic_keywords = ', '.join(top_keywords[:3])
        main_topic = f"The conversation was mainly about **{main_topic_keywords}** and related topics."
    else:
        main_topic = "The conversation topic could not be clearly identified."

    print(f"- {main_topic}")
    print(f"- Most common keywords: {', '.join(top_keywords)}")
