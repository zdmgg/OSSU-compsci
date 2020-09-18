import re

text = input('Enter file: ')

try:
    handle = open(text)
except:
    print('Error: file not found')
    exit()


ctr = 0
add = 0

try:
    for line in handle:
        line = line.strip()
        x = re.findall('^New Revision:\s([0-9]+)', line)
        if len(x) > 0:
            ctr = ctr + 1
            add = add + int(x[0])
except:
    print('Error: file not found')
    exit()

if ctr == 0:
    print('0')
elif ctr > 0:
    print(int(add/ctr))
