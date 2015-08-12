#!/usr/bin/env python3

def main():
    ch1 = input("char 1 : ")
    ch2 = input("char 2 : ")

    if ch1.isdigit() and ch2.isdigit():
        print("{} + {} = {}".format(ch1, ch2, int(ch1) + int(ch2)))
    else:
        print("Invalid")

if __name__ == "__main__":
    main()