import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving', url)
try:
    handle = urllib.request.urlopen(url)
except:
    print('Error: url not found')
    exit()
handle = handle.read().decode()
print('Retrieved', len(handle), 'characters')

try:
    stuff = ET.fromstring(handle)
except:
    print('Error: stuff not found')
    exit()
lst = stuff.findall('comments/comment')
print('Count:', len(lst))

sum = 0

for item in lst:
    sum = sum + int(item.find('count').text)

print(sum)
