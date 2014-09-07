"""
Purpose : problem119
Coder   : Himanshu Mishra (himanshu.m786@gmail.com)
"""


def problem119():
    count = 0
    for i in range(100000000, 1000000000):
        x = [ int(j) for j in list(str(i)) ]
        sum = 0
        for k in x:
            sum += k
        if check(i, sum):
            count += 1
            print(count, "--> ", i, sum)

def check(i, sum):
    for p in range(50):
        temp = sum**p
        flag = 0
        if temp == i:
            flag = 1
            break
        if temp >= i+3:
            break
    if flag ==  1:
        return True
    return False

if __name__ == '__main__':
    problem119()
