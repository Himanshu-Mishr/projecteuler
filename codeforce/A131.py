"""
Domain Name : Codeforces.com
Link        : http://codeforces.com/problemset/problem/131/A
Problem Name: A. cAPS lOCK
Method      : implementation, strings
Coder       : Himanshu-Mishr(himanshu.m786@gmail.com)
"""

def doNormal(x):
    """does normal """
    x = x.lower()
    print(x[0].upper() + x[1:])

def checkRest(x):
    '''
    return true if all the char in string are in Uppercase
    '''
    for i in x:
        if i.islower():
            break
    else:return True
    return False

def main():
    '''does all'''
    x = input()
    #print("Input :", x)
    #print("Enter : main()")

    if x[0].islower():
        #print("Enter : 1st lower char ")

        if checkRest(x[1:]):
            #print("Enter : checkRest()  is true")
            doNormal(x)

        else:
            #print("Enter : checkRest() was false")
            print(x)

        #print("-------------------------------------")
    elif checkRest(x):
        #print("Enter : All the character are in Upper Case")
        print(x.lower())

    else:
        #print("Enter : None of the case satisfied ")
        print(x)

if __name__ == '__main__':
    main()
