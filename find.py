import sys
import glob
from collections import Counter


def match(char_sum: list[str], query: str, word: str):
    if len(query) != len(word):
        return False

    for i in range(len(query)):
        if query[i] == "_":
            continue
        if query[i] != word[i]:
            return False

    return not Counter(word) - Counter(char_sum)


def search(char_sum: list[str], query: str, word_list: str):
    with open(word_list, "r") as word_file:
        for normalized_word in word_file:
            normalized_word = normalized_word.strip().upper()
            if match(char_sum, query, normalized_word):
                print(normalized_word)


def search_all(char_sum: str, query: str):
    normalized_char_sum = list(char_sum.upper())
    normalized_query = query.upper()
    for word_list in glob.glob("wordlists/*.txt"):
        search(normalized_char_sum, normalized_query, word_list)


charsum = sys.argv[1]

if len(sys.argv) > 2:
    query = sys.argv[2]
    search_all(charsum, query)
else:
    for n in range(3, len(charsum) + 1):
        query = "_" * n
        search_all(charsum, query)
