"""
Purpose : problem102
Coder   : Himanshu Mishra (himanshu.m786@gmail.com)
"""
import data102
points = data102.a

def main():
    '''problem 102, using data102.py'''
    count = 0
    for (x1, y1, x2, y2, x3, y3) in points:
        a = area(x1, y1, x2, y2, x3, y3)
        a1 = area(0, 0, x2, y2, x3, y3)
        a2 = area(x1, y1, 0, 0, x3, y3)
        a3 = area(x1, y1, x2, y2, 0, 0)
        print(a1, a2, a3, "SUM = ", a1 + a2 + a3," Actual area : ", a)
        if (a1 + a2 + a3) == a:
            count += 1
            print("Inside")
        else:
            print("Outside")
    print("Counter :> ", count)


def area(x1, y1, x2, y2, x3, y3):
    return (x1*(y2-y3) + x2*(y3-y1)+ x3*(y1-y2))/2.0
if __name__ == '__main__':
    main()
