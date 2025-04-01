# Get number of words in a text
# This function takes a string as input and returns the number of words in it.
def get_num_words(booktxt: str) -> int:
    num_words = len(booktxt.split())
    return num_words

# Get number of characters in a text
# This function counts the number of occurrences of each character in the text
# and returns a dictionary with the character as the key and the count as the value.
def get_num_characters(text: str) -> dict[str, int]:
    lowered_text = text.lower()
    char_count = {}
    for c in lowered_text:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count


def sort_on(dict):
    return dict["num"]

# This function takes a dictionary of character counts and returns a list of dictionaries
# with the character name and count, sorted in descending order by count.
# It uses the sort_on function as the `key` for sorting.
def print_report(d: dict[str, int]):
    report = []
    char = d.copy()
    for k, v in list(char.items()):
        char_count = {"name": k, "num": v}
        report.append(char_count)
    report.sort(reverse=True, key=sort_on)
    return report
