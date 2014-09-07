# Part Elf :  question 1
from fractions import Fraction
from decimal import Decimal
# counter
count = 0
i = 0
# main function
def main():
    global i
    # taking input

    # no of input
    for i in range(int(input())):
        # print("===================")
        partCase = input().split('/')
        global count
        count = 0
        if int(partCase[1]) % 2 == 0:
            recur(int(partCase[0])/int(partCase[1]))
        else:
            print("Case #%d:"%(i+1),'impossible')
        # print("Case #%d:"%(i+1), generation)

# manipulate and traverse tree

def recur(temp):
    global count, i
    count += 1
    result  = temp*2
    # print("------> ", result)
    if result > 1:
        dad = float(int(result))
        mom = dad - result
    else:
        dad = 0
        mom = result
    if dad == 1.0 or mom == 1.0:
        return print("Case #%d:"%(i+1),count)
    else:
        if dad > 0.0:
            recur(dad)
            recur(mom)
        else:
            recur(mom)

if __name__ == '__main__':
    main()
