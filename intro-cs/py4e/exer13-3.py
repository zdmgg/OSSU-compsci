import urllib.request, urllib.parse, urllib.error
import re
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
key = 42

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    if re.match('[Ee][Xx][Ii][Tt]', address):
        exit()

    parms = dict()
    parms['address'] = address
    parms['key'] = key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure to Retrieve')
        print(data)
        continue

    print('Place ID:', js['results'][0]['place_id'], '\n')
