import re

# Get number of words in a text
def get_num_words(booktxt: str) -> int:
    num_words = len(booktxt.split())
    return num_words

# ---------------------------------------------

def get_num_characters(text: str) -> dict[str, int]:
    lowered_text = text.lower()
    char_count = {}
    for c in lowered_text:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

# ---------------------------------------------

def sort_on(dict):
    return dict["num"]

def print_report(d: dict[str, int]):
    report = []
    char = d.copy()
    for k, v in list(char.items()):
        char_count = {"name": k, "num": v}        
        report.append(char_count)
    report.sort(reverse=True, key=sort_on)

    return report

# ---------------------------------------------
