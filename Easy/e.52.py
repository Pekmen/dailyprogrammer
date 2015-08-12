#!/usr/bin/env python3

def get_alpha_value(word):
    return(sum([ord(ch) - ord('a') + 1 for ch in word.lower()]))

def main():
    wordlist = ["Shoe", "Hat"]
    sortedlist = sorted(wordlist, key=get_alpha_value)
    print(sortedlist)
    
if __name__ == "__main__":
    main()