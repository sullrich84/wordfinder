import sys
import glob
from collections import Counter

def match(sum:list[str], pattern:str, payload:list[str]):
    if len(pattern) != len(payload):
        return False

    for i in range(len(pattern)):
        if pattern[i] == "_" or "-":
            continue
        if pattern[i] != payload[i]:
            return False

    return not Counter(payload) - Counter(sum)

def search(sum:list[str], pattern:list[str], filename:str):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().upper()
            if match(sum, pattern, line):
                print(line)

def search_all(sum:str, word:str):
    sum = list(sum.upper()) 
    pattern = list(word.upper())
    for wordlist in glob.glob("wordlists/*.txt"):
        search(sum, pattern, wordlist)


charsum = sys.argv[1]

if len(sys.argv) > 2:
    query = sys.argv[2]
    search_all(charsum, query)
else: 
    for n in range(3, len(charsum) +1):
        query = "_" * n
        search_all(charsum, query)

