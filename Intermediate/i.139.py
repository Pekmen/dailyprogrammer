import zipfile

chars = ('abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')
num_seq = raw_input().split()
targw = ''.join([chars[int(seq[0]) - 2][len(seq) - 1] for seq in num_seq])

zf = zipfile.ZipFile('british.zip')
for f in zf.namelist()[:2]:
    print '\n'.join([w for w in zf.read(f).split() if w.lower().startswith(targw)])
