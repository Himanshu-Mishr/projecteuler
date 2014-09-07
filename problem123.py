"""
Purpose : problem 123
Coder   : Himanshu Mishra (himanshu.m786@gmail.com)
"""
import mathTools

def main():
    '''problem 123'''
    count = 0
    for i in range(2, 1000000):
        if mathTools.checkPrime(i):
            count += 1
            if count%2 != 0:
                if ((i-1)**count + (i+1)**count) % i**2 >= 10000000000:
                    print(count)
                    break

if __name__ == '__main__':
    main()
