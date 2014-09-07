#import time
import prime
p = prime.a

def isPrime(i):
    x = i//2
    while x > 0:
        if i%x == 0:

            break
        x -= 1
    else:return True
    return False

def main():
    alist = []
    for i in p:
        for j in p:
            if ((i+j) in p) and ((j+i) in p) and ( int(i) < int(j)):
                print(i,j)
                alist.append([i,j])
    group = []
    for i in alist:
        for j in alist:
            for k in alist:
                if (i[0] in j) and (i[1] in k) and (j[1] in k) and (i[1] != j[1]) and (j[0] != k[0]) and (i[1] != j[0]) and (j[1] != k[0]):
                    print(i,j,k)
                    group.append([i,j,k])

if __name__ == '__main__':
    main()

'''

'''
