# Requires regex-sum txts

import re

text = input('Enter file name: ')
handle = open(text)

total = 0

for line in handle:
    line = line.strip()

    x = re.findall('[0-9]+', line)

    if len(x) > 0:
        for i in x:
            total = total + int(i)

print(total)
