"""
Purpose : problem 102
Coder   : Himanshu Mishra (himanshu.m786@gmail.com)
"""
import data102

def main():
    '''problem 102'''
    count = 0
    for i in data102.a:
        p0x = i[0]
        p0y = i[1]
        p1x = i[2]
        p1y = i[3]
        p2x = i[4]
        p2y = i[5]
        px  = 0
        py  = 0
        if (p1x-p0x) != 0:
            t = (py-p0y)/((( (p1y-p0y)*( (px-p0x)-(p2x-p0x) ) )/(p1x-p0x) ) + (p2y-p0y))
            s = ((px-p0x)-((p2x-p0x)*t))/(p1x-p0x)
            if 1-s-t > 0:
                count += 1
                print(s,t)
    print(count)
if __name__ == '__main__':
    main()
