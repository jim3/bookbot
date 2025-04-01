import sys
from stats import get_num_characters, get_num_words, print_report

NUM_ARGS = 2


def get_book_text(filepath: str) -> str:
    try:
        with open(filepath, "r") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: An error occurred while reading the file {filepath}.")
        sys.exit(1)
    return text


def process_report(report) -> None:
    for r in report:
        if r["name"].isalpha():
            print(f"{r['name']}: {r['num']}")


def main() -> None:
    if len(sys.argv) != NUM_ARGS:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    numwords = get_num_words(text)
    char_counts = get_num_characters(text)
    report = print_report(char_counts)
    process_report(report)


if __name__ == "__main__":
    main()
