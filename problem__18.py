"""
Purpose : problem18
Coder   : Himanshu Mishra (himanshu.m786@gmail.com)
"""
import time
import data18

matrix = data18.a
sum = 0
max = 0

def recursion(x, y):
    global sum, max
    print(matrix[x][y], " -> ", end='')
    sum += matrix[x][y]

    # to clear the sum index reaches to end of matrix
    if x == 14 or y == 14:
        print()
        # print("SUM : ", sum)
        sum = 0

    # prints the max sum found latest
    if sum > max:
        max = sum
        print("MAX : ", max)

    # this controls the recursion
    if x < 14 and y < 14:pass
    else:return "DONE"

    # this controls the moves
    recursion(x+1, y)
    recursion(x+1, y+1)

def main():
    '''uses the data18.py'''
    recursion(0, 0)

if __name__ == '__main__':
    main()
