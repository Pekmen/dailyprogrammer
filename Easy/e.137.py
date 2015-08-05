#!/usr/bin/env python

def string_trans(txt):
     with open(txt, 'r') as f:
        lines = map(str.strip, f.readlines()[1:])
        mx = len(max(lines, key=len))
        for i in range(mx):
            l = ''
            for line in lines:
                try:
                    l += line[i]
                except :
                    l += ' '
            print l 
                        

string_trans('lel.txt')
