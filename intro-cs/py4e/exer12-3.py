import urllib.request, urllib.parse, urllib.error, ssl
from bs4 import BeautifulSoup

url = input('Enter URL: ')

try:
    test1 = urllib.request.urlopen(url)
except:
    print('Error: url not found')

count = input('Enter count: ')
pos = input('Enter position: ')

for i in range(int(count)):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url)
    print('Retrieving:', url)
    soup = BeautifulSoup(html, 'html.parser')

    lst = list()
    tags = soup('a')

    for tag in tags:
        lst.append(tag.get('href', None))

    url = lst[int(pos)]
