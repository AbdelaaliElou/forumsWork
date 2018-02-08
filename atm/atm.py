# 277 ---> 772 # 275 ---> 572
# def rev_request(request):
#     return int(str(request)[::-1])
#
#
# def print_given(n, p):
#     # print (p)
#     # print ('n', n)
#     # print 'given', given
#     for i in range(0, n):
#         print 'given', 10**p
#
#
# def res(request):
#     # rev = request
#     if request != 0:
#         # print ('rev', request)
#         print_given(request % 10, len(str(request)) - 1)
#         request = int(request / 10)
#         res(request)
#
#
# res(rev_request(500))

amount = 500


def rev(req):
    return str(req)[::-1]


def print_given(single, power):
    res = - 1
    if int(single) >= 5 and power != 2:
        print 'given', 5 * 10**power
        res = int(single) - 5
    elif int(single) < 5 and power != 2:
        res = int(single)

    if 4 >= res > 0 and power == 0:
        print 'given', res

    if power == 1:
        for i in xrange(0, int(single)-5):
            print 'given', 10**power
    if power == 2:
        for i in xrange(0, int(single)):
            print 'given', 10**power


def atm_func(request):
    # if request != 0:
    #     print_given(request % 10, len(str(request)) - 1)
    #     request = request / 10
    #     atm_func(request)
    # request = rev(request)
    global amount
    print 'Requested:', request
    if 0 < request <= amount:
        length = len(rev(request))
        for i in xrange(length):
            print_given(rev(request)[length - i - 1], length - i - 1)
        amount -= request
    else:
        print 'Amount is not valid'





























