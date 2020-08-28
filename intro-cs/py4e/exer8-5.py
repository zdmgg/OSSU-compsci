# Requires mbox-short.txt

fname = input('Enter a file name: ')
file = open(fname)
counter = 0

for line in file:
    line = line.rstrip()
    if line == '':
        continue
    if 'From:' in line:
        continue
    if line.startswith('From'):
        words = line.split()
        print(words[1])
        counter = counter + 1

print('There were', counter, 'lines in the file with From as the first word.')
