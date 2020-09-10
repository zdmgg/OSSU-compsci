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
        place = words[1].split('@')
        add.append(place[1])

for word in add:
    counts[word] = counts.get(word, 0) + 1
print(counts)
