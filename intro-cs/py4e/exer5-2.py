largest = None
smallest = None

while True:
    num = input('Enter a number: ')
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue
    if (largest is None) or (smallest is None):
        largest = num
        smallest = num
    elif (largest is not None) and (smallest is not None):
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

print('Maximum is', largest)
print('Minimum is', smallest)
