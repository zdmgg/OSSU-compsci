largest = None
smallest = None
numbers = list()

while True:
    num = input('Enter a number: ')

    if num == "done":
        if numbers == []:
            max = '(no input)'
            min = '(no input)'
        else:
            max = max(numbers)
            min = min(numbers)
        break

    try:
        num = int(num)
    except:
        print('Invalid input')
        continue

    num = float(num)
    numbers.append(num)
print('Maximum is', max)
print('Minimum is', min)
