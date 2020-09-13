alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
approved = list()
counts = dict()
sortedlist = list()

fhand = input('Enter a file name: ')
handle = open(fhand)

for line in handle:
    line.strip()
    words = line.split()

    for word in words:
        word = word.lower()
        wordtemp = tuple(word)

        for i in wordtemp:
            if i in alphabet:
                approved.append(i)

for letter in approved:
    counts[letter] = counts.get(letter, 0) + 1

for k, v in counts.items():
    newtup = (v, k)
    sortedlist.append(newtup)

sortedlist = sorted(sortedlist, reverse = True)

for k, v in sortedlist:
    print(k, v)
