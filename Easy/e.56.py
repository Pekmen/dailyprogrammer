import string

seq = ""
with open("text.txt", "w") as fn:
    for i in range(26):
        seq = "{p}{a}{p}".format(p = seq, a = string.ascii_lowercase[i])
        fn.write(seq)
