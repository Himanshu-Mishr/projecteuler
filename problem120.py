"""
Purpose : problem 120
Coder   : Himanshu Mishra (himanshu.m786@gmail.com)
"""


def problem120():
    sum = 0
    for a in range(3, 1001):
        x = sorted([((a-1)**n + (a+1)**n) % a**2 for n in range(1, 2001, 2)])[-1]
        sum += x
        print( a, x)

    print("--------->", sum)


if __name__ == '__main__':
    problem120()
