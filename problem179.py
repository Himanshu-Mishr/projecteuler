"""
Purpose : problem179
Coder   : Himanshu Mishra (himanshu.m786@gmail.com)
"""


def problem179():
    count = 0
    x = divisor(1)      # n
    for i in range(2, 10000000):
        print(i)
        y = divisor(i)  # n+1
        if x == y:
            count += 1
            #print(i-1, i, " -----> ", x)
        x = y
    print(count)

def divisor(i):
    y = i//2
    count = 0
    while y>=1:
        if i%y==0:
            count += 1
        y -= 1
    return count+1


if __name__ == '__main__':
    problem179()
