import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retrieving', url)

try:
    handle = urllib.request.urlopen(url)
except:
    print('Error: url not found')
    exit()

try:
    handle = handle.read().decode()
except:
    print("Error: can't decode url")
    exit()

print('Retrieved', len(handle), 'characters')

try:
    info = json.loads(handle)
except:
    print('Error: JSON not found')
    exit()

ctr = 0
sum = 0

for item in info['comments']:
    sum = sum + item['count']
    ctr = ctr + 1

print('Sum:', sum)
print('Count:', ctr)
