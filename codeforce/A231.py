"""
Domain Name : Codeforces.com
Link        : http://codeforces.com/problemset/problem/231/A
Problem Name: A. Team
Method      : brute force, greedy, implementation
Coder       : Himanshu-Mishr(himanshu.m786@gmail.com)
"""

def main():
    '''does all'''
    count = 0
    for i in range(int(input())):
        a = [int(j) for j in input().split(" ")]
        if a[0] + a[1] + a[2] >= 2:count += 1

    print(count)

if __name__ == '__main__':
    main()
