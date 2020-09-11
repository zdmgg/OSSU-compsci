counts = dict()
add = list()
high = list()

file = input('Enter file name: ')
handle = open(file)

for line in handle:
    line.rstrip()
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        words = line.split()
        add.append(words[1])

for word in add:
    counts[word] = counts.get(word, 0) + 1

for k, v in counts.items():
    newtup = (v, k)
    high.append(newtup)

high = sorted(high, reverse = True)
print(high[0])
