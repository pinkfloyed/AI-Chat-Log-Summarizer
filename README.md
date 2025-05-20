# **AI-Chat-Log-Summarizer**

**AI Chat Log Summarizer** is a Python-based tool that reads `.txt` chat logs between a user and an AI, parses the conversation, and generates concise text-based summaries. It supports multiple keyword extraction methods and batch processing of multiple logs, and produces a simple summary that includes :

- Message counts
- Frequently used keywords
- Summarize chat log conversation

This project demonstrates basic Natural Language Processing (NLP) capabilities using Python and NLTK.

---

## 📌 **Project Features**

✅ Parse chat logs  
✅ Separate User and AI messages  
✅ Count message statistics  
✅ Extract top keywords (excluding stop words)  
   - NLTK (word frequency-based)
   - TF-IDF (unigram + bigram analysis)
✅ Generate clean, readable summaries
✅ Save summaries to .txt files automatically 

--- 

## 📂 **Project Structure**

```text
AI-Chat-Log-Summarizer/
├── data/                       # Folder containing input .txt chat logs
│   ├── chat.txt
│   └── chat1.txt ...
├── summaries/                  # Folder where summary output files are saved
├── chat_parser.py              # Module to parse chat logs into user and AI messages
├── main.py                     # Entry point to run the chat summarizer
├── summary_generator.py        # Module to generate conversation summaries with stats and keywords
├── utils.py                    # Helper utilities, including keyword extraction
├── requirements.txt            # Project dependencies
├── README.md                   # Project overview and usage instructions
├── LICENSE                     # Licensing information
├── .gitignore                  # Specifies untracked files for Git
├── tfidf_keywords.py           # Module for TF-IDF keyword extraction
└── env                         # Environment variables/configuration folder

```
---

## 📥 **Input Format**

Each chat log file should follow this format :

- User: Hello!
- AI: Hi! How can I assist you today?
- User: Can you explain what machine learning is?
- AI: Certainly! Machine learning is a field of AI that allows systems to learn from data.

---

## ⚙️ **How It Works**

1. **Chat Log Parsing**  
   Extracts and stores messages by speaker role (`User:` vs `AI:`).

2. **Message Statistics**  
   Counts the number of total exchanges, user messages, and AI messages.

3. **Keyword Analysis**  
   - Identifies top 5 frequently used words  
   - Ignores stop words like "the", "is", "and"
   - nltk: Simple word frequency using NLTK, excludes stop words 
   - tfidf: Uses scikit-learn to compute TF-IDF scores for top keywords

4. **Summary Output**  
   Displays:
   - Number of exchanges  
   - Key discussion topics  
   - Most common keywords
   - Saves combined summaries to:
         - summaries/all_nltk_summaries.txt 
         - summaries/all_tfidf_summaries.txt

---

## **Installation Steps :**
1. Clone the repository :
   ```bash
   git clone <repository-url>
   cd project-root

2. Set up a virtual environment :
   ```bash
   python3 -m venv env

3. Activate the virtual environment :
   ```bash
   env\Scripts\activate

4. Install dependencies :
   ```bash
   pip install -r requirements.txt

5. Ensure nltk is installed and stopwords downloaded :
   ```bash
   import nltk
   nltk.download('stopwords')
   
### **Steps to Run the Project :**
   1. Run this command in the terminal :
   ```bash
   python main.py
   ```
   2. You’ll be prompted to choose a keyword method :
   ```bash
   Choose keyword extraction method (nltk / tfidf) :
   ```
Summaries will be printed and saved to the summaries/ folder

---

## 📦 **Dependencies**
   - Python 3.11 
   - NLTK 
   - scikit-learn
   - numpy

---

### 🔍 **Keyword Extraction Methods Used**

1. **NLTK-Based Frequency Analysis**  
   - Uses tokenization, stopword removal, and frequency counting.
   - Detects both single words (unigrams) and two-word phrases (bigrams) with high likelihood scores.

2. **TF-IDF (Term Frequency–Inverse Document Frequency)**  
   - Identifies the most relevant terms in the conversation using weighted importance scores.
   - Supports both unigrams and bigrams.

3. **Dynamic Method Selection**  
   - Users can choose between `nltk` or `tfidf` at runtime to analyze chat logs, allowing for flexible summarization.

---

## 🔍 **Key Insights :**
- NLTK method provides more meaningful, context-aware keywords for short chat conversations
- TF-IDF method captures statistically significant terms but may include generic words like "data" or "code".
- So based on the chat logs messages dataset NLTK performs better for summarization of small to medium chat logs

---

## 📝 **License**
- This project is licensed under the MIT License.

