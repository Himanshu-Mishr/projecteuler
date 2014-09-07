"""
Purpose : problem 112
Coder   : Himanshu Mishra (himanshu.m786@gmail.com)
"""
import time

def main():
    '''problem 112'''
    start = time.time()
    adc = 81
    bc = 1

    for i in range(100, 1000):
        x = str(i)
        if (x[0] <= x[1] and x[1] <= x[2]) or (x[0] >= x[1] and x[1] >= x[2]) :
            adc += 1
            print("adc : ", i)
        else:
            bc += 1
            print("bc : ", i)
        print(">", i," proprotion : ", (adc/bc)*100)
    print("TIME TAKEN : ", time.time() - start)
if __name__ == '__main__':
    main()
