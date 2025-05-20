from chat_parser import parse_chat
from utils import extract_keywords
from summary_generator import generate_summary
import os

def save_summary_to_file(summary_lines, output_path):
    """
        Saves a list of summary lines to a specified text file.

        Args:
            summary_lines (list of str): Lines of the summary to write to file.
            output_path (str): Path to the output file where summary will be saved.

        Prints:
            Confirmation message on successful save or error message if failed.
    """

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            for line in summary_lines:
                f.write(line + "\n")
        print(f"\nSummary saved to: {output_path}")
    except Exception as e:
        print(f"Error saving summary to file: {e}")


def main():
    """
        Main script to process and summarize multiple chat logs.

        Functionality:
        - Prompts the user to select a keyword extraction method ("nltk" or "tfidf").
        - Reads and parses all `.txt` chat files from the `data/` folder.
        - Extracts user and AI messages from each file.
        - Generates a summary for each chat log, including:
            - Total exchanges
            - Count of user and AI messages
            - Most common keywords
            - Main topic discussed
        - Prints each summary to the terminal.
        - Saves summaries to separate output text files:
            - One for each method (e.g., `summary_nltk.txt`, `summary_tfidf.txt`).
    """

    chat_folder = "data"
    summary_folder = "summaries"
    os.makedirs(summary_folder, exist_ok=True)

    method = input("Choose keyword extraction method (nltk / tfidf) : ").strip().lower()
    if method not in ["nltk", "tfidf"]:
        print("Invalid method selected. Defaulting to 'nltk'.")
        method = "nltk"

    output_file_path = os.path.join(summary_folder, f"all_{method}_summaries.txt")

    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(f"Summary report for method: {method}\n\n")


    for filename in os.listdir(chat_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(chat_folder, filename)
            print(f"\nProcessing: {filename}")
            try:
                user_msgs, ai_msgs = parse_chat(file_path)
                summary_lines = generate_summary(user_msgs, ai_msgs, top_n=5, method=method, return_lines=True)

                for line in summary_lines:
                    print(line)

                with open(output_file_path, "a", encoding="utf-8") as f:
                    f.write(f"File: {filename}\n")
                    for line in summary_lines:
                        f.write(line + "\n")
                    f.write("\n" + "-" * 40 + "\n\n")

            except Exception as e:
                print(f"Failed to process '{filename}': {e}")

    print(f"\nSummary saved to: {output_file_path}")

if __name__ == "__main__":
    main()
