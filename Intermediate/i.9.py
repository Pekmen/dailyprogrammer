#!/usr/bin/env python3

 
def myreplace(target, replacement, filename):
    replaced = []
    with open(filename) as fn:
        for line in fn.readlines():
            replaced.append(line.replace(target, replacement))
    return(replaced)

def list_to_file(l, filename):
    with open(filename, "w+") as fn:
        for line in l:
            fn.write(line)

def main():
    filename = "text.txt"
    filename_new = "new_text.txt"
    target = input("Enter a target string:\n")
    replacement = input("Enter a replacement:\n")

    lines_new = myreplace(target, replacement, filename)
    list_to_file(lines_new, filename_new)


if __name__ == "__main__":
    main()