from decimal import *

# main function
def main():

    # getcontext().prec set the number of precision
    getcontext().prec = 100
    for i in range(1,1001):
        print("Normal > ", 1/i)
        print(i , " Repeat ", repeat(str(Decimal(1)/Decimal(i))))


# repeat function : finds the number of recurring cycle
def repeat(s):return s

if __name__ == '__main__':
    main()
