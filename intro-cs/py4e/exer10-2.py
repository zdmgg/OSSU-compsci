fname = input('Enter a file name: ')
handle = open(fname)

hour = list()
counts = dict()
sort = list()

for line in handle:
    line.rstrip()
    if line.startswith('From:'): continue
    if line.startswith('From'):
        words = line.split()
        time = words[5].split(':')
        hour.append(time[0])

for h in hour:
    counts[h] = counts.get(h, 0) + 1

for k, v in counts.items():
    sort.append((k, v))

sort = sorted(sort)
print(sort)

for k, v in sort:
    print(k, v)
