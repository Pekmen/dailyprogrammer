#!/usr/bin/env python3

##
#  [Easy] #213
#
#  Celular Automata
#
#  https://www.reddit.com/r/dailyprogrammer/comments/3jz8tt/20150907_challenge_213_easy_cellular_automata/
##


def draw(cells):
    for i in range(len(cells)):
        print("x" if cells[i] == 1 else " ", end="")
    print("\t")
    

def main():
    steps = 25
    prevg = [int(x) for x in input("insert cells seed >")]
    glen = len(prevg)
    draw(prevg)
    for _ in range(steps):
        nextg= [int(prevg[i-1] != prevg[i+1]) for i in range(1, glen - 1)]
        nextg.append(0)
        nextg.insert(0, 0)
        draw(nextg)
        prevg = nextg    
    

if __name__ == "__main__":
    main()