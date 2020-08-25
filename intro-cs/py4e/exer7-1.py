# Requires mbox.txt and/or mbox-short.txt

fname = input('Enter a file name: ')
file = open(fname)
for line in file:
    line = line.rstrip().upper()
    print(line)
