# coder : Himanshu Mishra
# Math tools :
#
# this script contain function :-

def checkPrime(i):
    '''returns True or False'''
    y = i//2
    while y>1:
        if i%y == 0:
            break
        y -= 1
    else:
        return True
    return False

def pandigital( x = 123456789,y = 987654322):
    ''' prints as string'''
    for i in range(x, y):
        i_str = str(i)
        alist = list(i_str)
        if len(alist) == len(set(alist)) and ('0' not in alist):
            print(i)

def breakdown(i):
    '''accept str, returns list'''

