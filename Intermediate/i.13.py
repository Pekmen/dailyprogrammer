#!/usr/bin/env python

textfile = "text.txt"
inpstr = "hello!"

with open(textfile, "w") as fn:
    fn.write(inpstr[::-1])