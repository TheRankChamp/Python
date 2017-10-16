balance = 32
annualInterestRate = 0.2

lowParam = round(balance/12)
upParam = round(((balance*annualInterestRate)+balance )/12)
mid = (lowParam + upParam)/2
payment = balance/12
print('lower parameter ----> ' + str(lowParam))
print('upper parameter ----> ' + str(upParam))

lowParam = round(balance / 12)
upParam = round(((balance * annualInterestRate) + balance) / 12)

while balance/12 > 0:

    mid = (lowParam + upParam) / 2
    payment = balance / 12

    if (balance/12 - lowParam) > 0:
        lowParam = upParam
        upParam = (upParam + mid)
        payment = upParam
        print(upParam, lowParam, balance)

    else:
        upParam = lowParam
        lowParam = (lowParam - mid)
        payment = lowParam
        print(upParam, lowParam, balance)
