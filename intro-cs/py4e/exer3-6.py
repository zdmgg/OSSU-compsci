def computepay(hrs, rate):
    if hrs > 40 :
        excess = hrs - 40
        hrs = 40
        pay = hrs * rate
        pay = (excess * rate * 1.5) + pay
        return pay
    else :
        pay = hrs * rate
        return pay

try:
    hrs = input("Enter Hours: ")
    hrs = float(hrs)
    rate = input("Enter Rate: ")
    rate = float(rate)

    pay = computepay(hrs, rate)
    print('Pay:', pay)
except:
    print('Error, please enter numeric input')
