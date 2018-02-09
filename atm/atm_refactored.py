# balacne = 500


def withdraw(balance, request):
    if request < 0:
        print 'pls enter a positive number :)'
        return balance
    if request > balance:
        print('we can\'t give that amount of value!!')
        return balance
    print 'current balance =', balance
    balance -= request
    while request > 0:
        if request >= 100:
            request -= 100
            print 'given 100'
        elif request >= 50:
            request -= 50
            print 'given 50'
        elif request >= 10:
            request -= 10
            print 'given 10'
        elif request >= 5:
            print 'given', request
            request -= 5
        elif request < 5:
            print 'given', request
            request = 0
    return balance


balance = withdraw(5425425528728278, 5425425)
balance = withdraw(balance, 225)
print balance
balance = withdraw(balance, 666)
