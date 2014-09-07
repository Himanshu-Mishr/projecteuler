"""
Purpose : problem102
Coder   : Himanshu Mishra (himanshu.m786@gmail.com)
"""
import data102
points = data102.a

def main():
    '''data102.py'''
    for a1, a2, b1, b2, c1, c2 in points:

        #AB→B−A
        abx = b1 - a1
        aby = b2 - a2

        #BC→C−B
        bcx = c1 - b1
        bcy = c2 - b2

        #CA→A−C
        cax = a1 - c1
        cay = a2 - c2

        #AP→P−A
        apx = -1 * a1
        apy = -1 * a2

        #BP→P−B
        bpx = -1 * b1
        bpy = -1 * b2

        #CP→P−C
        cpx = -1 * c1
        cpy = -1 * c2

if __name__ == '__main__':
    main()
