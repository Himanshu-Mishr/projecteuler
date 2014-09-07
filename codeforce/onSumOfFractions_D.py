from fractions import Fraction

alist = []

def main():
    n = int(input())
    while n>0:
        work(int(input()))
        n -= 1
    return 0

def work(n):
    global alist
    sum = Fraction()
    for i in range(2, n+1):
        for j in alist:
            if i == j[0]:
                sum += j[1]
                break
        else:
            alist.append([i, Fraction(1, v(i)*u(i))])
            sum += Fraction(1, v(i)*u(i))

    print( sum.numerator, "/", sum.denominator, sep='')


# largest prime
def v(i):
    while i > 1:
        if checkPrime(i):
            return i
        i -= 1

# smallest prime
def u(i):
    i += 1
    while 1:
        if checkPrime(i):
            return i
        i += 1

# prime?
def checkPrime(y):
    x = y//2
    while x>1:
        if y%x == 0:break
        x -= 1
    else:return True
    return False

if __name__ == '__main__':
    main()
