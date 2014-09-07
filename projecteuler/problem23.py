import time
def main():
    a = []
    start = time.time()
    for i in range(28125):
        sum = 0
        x = i//2
        #print('----------------')
        #print(i," > ",end=' ')
        while x>0:
            if i%x == 0:
                sum += x
                #print(x,end=' ')
            x -= 1
        if sum > i:
            #print(i)
            a.append(i)
    b = []
    for i in a:
        for j in a:
            sum = i+j
            if sum < 28124:
                b.append(i+j)
    c = [i for i in range(1,28124)]
    d = set(c) - set(b)
    sum = 0
    for i in list(d):
        sum += i
    print("Total sum : ",sum)
    print("Time taken : ",time.time() - start)
if __name__ == '__main__':
    main()
