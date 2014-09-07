'problem 51 of project euler'


def problem51():
    'driver function'
    for i in range(2, 10000):

    return 0


def isPrime(i):
    'checks whether a number is prime or not'
    x = i//2
    while x > 1:
        if i%x == 0:
            break
        x -= 1
    else:
        return True
    return False

if __name__ == '__main__':
    problem51()
