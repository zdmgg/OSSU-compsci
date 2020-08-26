# Requires mbox-short.txt

fname = input('Enter a file name: ')
file = open(fname)

for line in file:
    line.strip()
    print(line)
    if line == '':
        print(Skipped, blacnk)
        continue
    if line.startswith('From:'):
        words = line.split()
        print(words)
        print(words[2])
