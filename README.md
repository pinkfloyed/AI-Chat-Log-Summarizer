# AI-Chat-Log-Summarizer

AI Chat Log Summarizer is a Python-based tool that reads `.txt` chat logs between a user and an AI, parses the conversation, and produces a simple summary that includes :

- Message counts
- Frequently used keywords
- Summarize chat log conversation

This project demonstrates basic Natural Language Processing (NLP) capabilities using Python and NLTK.

---

## 📂 Project Structure

```text
AI-Chat-Log-Summarizer/
├── data/
│   └── chat.txt                # Sample chat log input file
├── chat_parser.py              # Module to parse chat logs into user and AI messages
├── main.py                     # Entry point to run the chat summarizer
├── summary_generator.py        # Module to generate conversation summaries with stats and keywords
├── utils.py                    # Helper utilities, including keyword extraction
├── requirements.txt            # Project dependencies
├── README.md                   # Project overview and usage instructions
├── LICENSE                     # Licensing information
├── .gitignore                  # Specifies untracked files for Git
└── env                         # Environment variables/configuration folder
```
---

## 📌 Project Features

✅ Parse chat logs  
✅ Separate User and AI messages  
✅ Count message statistics  
✅ Extract top keywords (excluding stop words)  
✅ Generate a clean text-based summary 

## 📂 Input Format

Provide a `.txt` file in the following structure :

- User: Hello!
- AI: Hi! How can I assist you today?
- User: Can you explain what machine learning is?
- AI: Certainly! Machine learning is a field of AI that allows systems to learn from data.

---

## ⚙️ How It Works

1. **Chat Log Parsing**  
   Extracts and stores messages by speaker role (`User:` vs `AI:`).

2. **Message Statistics**  
   Counts the number of total exchanges, user messages, and AI messages.

3. **Keyword Analysis**  
   - Identifies top 5 frequently used words  
   - Ignores stop words like "the", "is", "and"  
   - Uses NLTK with optional bigram support

4. **Summary Output**  
   Displays:
   - Number of exchanges  
   - Key discussion topics  
   - Most common keywords

---

## 📦 Requirements

- Python 3.6+
- NLTK

Install the required packages:
```bash
pip install nltk
```

