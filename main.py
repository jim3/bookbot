import sys
from stats import get_num_characters, get_num_words, print_report

NUM_ARGS = 2

def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as f:
        text = f.read()
    return text

def main() -> None:
    if len(sys.argv) != NUM_ARGS:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    numwords = get_num_words(text)
    char_counts = get_num_characters(text)
    report = print_report(char_counts)
    
    for r in report:
        if r['name'].isalpha():
            print(f"{r['name']}: {r['num']}")

if __name__ == "__main__":
    main()
