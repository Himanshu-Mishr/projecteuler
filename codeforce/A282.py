"""
Domain Name : Codeforces.com
Link        : http://codeforces.com/problemset/problem/282/A
Problem Name: A. Bit++
Method      : implementation
Coder       : Himanshu-Mishr(himanshu.m786@gmail.com)
"""

def main():
    ''''''
    x = 0
    for i in range(int(input())):
        astr = input()
        if '+' in astr:x += 1
        else:x -= 1
    print(x)
if __name__ == '__main__':
    main()
