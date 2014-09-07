"""
Purpose : problem 120
Coder   : Himanshu Mishra (himanshu.m786@gmail.com)
"""


def problem120():
    sum = 0
    for a in range(3, 1001):
        for n in range(1, 10001, 2):
            s = ((a-1)**n + (a+1)**n) % a**2
            print( a, n, s)

    print("--------->", sum)


if __name__ == '__main__':
    problem120()
