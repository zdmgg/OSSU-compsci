import re

text = input('Enter a regular expression: ')
handle = open('mbox.txt')

ctr = 0

for line in handle:
    line = line.strip()
    x = re.findall(text, line)
    if len(x) > 0:
        ctr = ctr + 1

print('mbox.txt had', ctr, 'lines that matched', text)
