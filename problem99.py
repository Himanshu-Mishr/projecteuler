"""
Purpose : problem99 of project euler
Coder   : Himanshu Mishra (himanshu.m786@gmail.com)
"""
import math
import time
import dataFor99

s = dataFor99.a

def main():
    '''killing problem 99 with log'''
    count = 0
    alist = []
    start = time.time()
    for (p, q) in s:
        count += 1
        z = q * math.log10(p)
        print(count, "--> ", z)
        alist.append(z)

    alist.sort()
    print(alist[-1])

    print("time taken : ", time.time() - start)

if __name__ == '__main__':
    main()
