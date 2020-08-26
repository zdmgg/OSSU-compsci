#Requires romeo.txt

fname = input('Enter file: ')
file = open(fname)
words = list()
for line in file:
    spline = line.split()
    for spword in spline:
        if spword not in words:
            words.append(spword)
words.sort()
print(words)
