#!/usr/bin/env python3

import string


def titlecase(title, exceptions):
    title=title.split();
    return [word.lower().capitalize() if word.lower() in exceptions else word.lower() for word in title]


def main():
    exceptions = ['are', 'is', 'in', 'your', 'my'];
    title = ("THE vitamins ARE IN my fresh CALIFORNIA raisins");
    print(titlecase(title, exceptions));


if __name__ == "__main__":
    main()
