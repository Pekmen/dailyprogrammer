#!/usr/bin/env python3

def get_factors(n):
    aux = 2
    factors = []
    while n != 1:
        if n % aux == 0:
            factors.append(aux)
            n = n / aux
        else:
            aux += 1
    return factors

def main():
    n = 14
    print("{} = {}".format(n, " * ".join(str(x) for x in get_factors(n))))


if __name__ == "__main__":
    main()