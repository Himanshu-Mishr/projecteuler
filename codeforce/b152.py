"""
Domain Name : Codeforces.com
Link        : http://codeforces.com/problemset/problem/158/B
Problem Name: B. Taxi
Method      : greedy, implementation
Coder       : Himanshu-Mishr(himanshu.m786@gmail.com)
"""

# library to import

def main():
    '''
    about :
    '''
    n = input()
    atext = input()
    group = [int(i) for i in atext.split(' ')]
    print(group)
    a = group[:]
    count = 0

    # remove 4 from the list
    print('------------------------')
    for i in group:
        print(a)
        if i == 4:
            a.remove(4)
            count += 1
    print("after removing 4 no of taxi : ", count)
    group = a[:]

    # removing 3 and 1 in pair from the list
    print('------------------------')
    for i in group:
        print(a)
        if i
if __name__ == '__main__':
    main()
