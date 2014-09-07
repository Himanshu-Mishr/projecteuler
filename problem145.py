"""
Purpose : problem 145
Coder   : Himanshu Mishra (himanshu.m786@gmail.com)
"""
import time

odd = [ '1', '3', '5', '7', '9']
def main():
    '''problem 145'''
    start = time.time()
    count = 0
    #seven
    for i in range(1000000000):
        x = str(i)
        # checking zero
        if i%10!=0:
            reversed(x)
            y = ''
            for j in x:y = j + y
            z = list(str(int(x)+int(y)))
            # z is made of odd numbers
            if checkDigitOdd(z):
                count += 1
    print(count)
    print("time taken> ", time.time() - start)
    return 0

def checkDigitOdd(z):
    for i in z:
        if i not in odd:
            return False
    else:
        return True

if __name__ == '__main__':
    main()
