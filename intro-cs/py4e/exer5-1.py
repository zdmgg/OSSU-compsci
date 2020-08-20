score = None
count = 0
total = 0
average = 0

while score != 'done':
    try:
        number = input('Enter a number: ')
        if number == 'done':
            break
        number = float(number)
        total = total + number
        count = count + 1
        average = total/count
    except:
        print('Invalid input')

print(total, count, average)
