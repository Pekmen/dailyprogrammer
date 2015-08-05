#!/usr/bin/env python3

import string, time

def main():
    filename = "text.txt"
    with open(filename) as f:
        exclude = set(string.punctuation+"\x00")
        text = (ch.lower() for ch in f.read() if ch not in exclude and not ch.isdigit())
    words = ["".join(sorted(w)) for w in set("".join(text).split())]
    anag_count = len(words) - len(set(words))
    print(anag_count)


if __name__ == "__main__":
     main()