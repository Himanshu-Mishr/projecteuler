"""
Domain Name : Codeforces.com
Link        : http://codeforces.com/problemset/problem/82/A
Problem Name: A. Double Cola
Method      : implementation, math
Coder       : Himanshu-Mishr(himanshu.m786@gmail.com)
"""
import time

def main():
    '''
    '''
    start = time.time()
    cans = input()
    a = 'Sheldon'
    b = 'Leonard'
    c = 'Penny'
    d = 'Rajesh'
    e = 'Howard'

    queue = ['a', 'b', 'c', 'd', 'e']
    for i in range(int(cans)):
        x = queue[0]
        queue = queue[1:]
        queue.append(x)
        queue.append(x)
    else:print(x)
    print("Time taken :", time.time() - start)
if __name__ == '__main__':
    main()
