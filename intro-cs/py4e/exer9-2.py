counts = dict()
day = list()

file = input('Enter file name: ')
handle = open(file)

for line in handle:
    line.rstrip()
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        words = line.split()
        day.append(words[2])

for word in day:
    counts[word] = counts.get(word, 0) + 1
print(counts)