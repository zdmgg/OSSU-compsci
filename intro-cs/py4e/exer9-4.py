counts = dict()
add = list()

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

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or bigcount < count:
        bigcount = count
        bigword = word

print(bigword, bigcount)
