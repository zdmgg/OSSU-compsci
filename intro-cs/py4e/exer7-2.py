# Requires mbox.txt and mbox-short.txt

total = 0
count = 0

fname = input('Enter the file name: ')

if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()

try:
    file = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

for line in file:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        num = line[21:]
        num = float(num)
        total = total + num
        count = count + 1

average = total / count
print('Average spam confidence:', average)
