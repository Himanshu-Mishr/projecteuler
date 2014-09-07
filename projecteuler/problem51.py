#!/usr/bin/python3
# coder : Himanshu Mishra
# about : problem 51
# algorithm used : not decided till now
# links : http://projecteuler.net/problem=51
import time
def primechecker(num):
    """
    primechecker() :checks prime or not
    """
    x= num//2
    while x>1:
        if num%x == 0:break
        x -= 1
    else:return True
    return False

def main():
    start = time.time()
    b = [str(i) + str(j) for i in range(1000,9999) for j in [1,3,7,9] if primechecker(int(str(i) + str(j)))]
    print(b)
    print("time taken :",time.time() - start)


# this is the standard biolerplate that calls the main() function.
if __name__ == '__main__':
    main()
