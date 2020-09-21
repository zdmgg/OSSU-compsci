import urllib.request, urllib.parse, urllib.error, re
from bs4 import BeautifulSoup

text = input('Enter: ')
fhand = urllib.request.urlopen(text).read()
soup = BeautifulSoup(fhand, 'html.parser')

spans = soup('span')

total = 0
ctr = 0

for span in spans:
    total = total + int(span.contents[0])
    ctr = ctr + 1

print('Count:', ctr)
print('Sum:', total)
