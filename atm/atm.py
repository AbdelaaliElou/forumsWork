class Atm:
    def __init__(self, atm_balance, bank_name):
        self.atm_balance = atm_balance
        self.bank_name = bank_name

    def withdraw(self, request):
        welcome_to = 'Welcome to ' + self.bank_name
        current_balance = 'Current balance is ' + str(self.atm_balance)
        print welcome_to
        print current_balance
        print '='*len(welcome_to+current_balance)
        if request > self.atm_balance:
            print 'we can\'t give that amount of value!!'
        elif request < 0:
            print 'pls enter a positive number.'
        else:
            self.atm_balance -= request
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
        print '=' * len(welcome_to + current_balance)
        return self.atm_balance

