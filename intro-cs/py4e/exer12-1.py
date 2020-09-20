import socket

url = input('Enter URL: ')
main = url.split('/')

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((main[2], 80))
except:
    print('URL not found')
    exit()

cmd = ('GET ' + url + ' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
