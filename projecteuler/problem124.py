'''
problem 124 project euler
'''
import time
import pprint
a = {'0':0}
def main():

    flist = []

    for i in range(1,20):
        a[str(i)] = 1

    start = time.time()
    for i in range(18):
        for j in range(12):
            for k in range(9):
                for l in range(7):
                    for m in range(6):
                        for n in range(6):
                            for o in range(6):
                                x = 2**i * 3**j * 5**k * 7**l * 11**m * 13**n * 17**o
                                if x <= 100000:
                                    y = 2**a[str(i)] * 3**a[str(j)] * 5**a[str(k)] * 7**a[str(l)] * 11**a[str(m)] * 13**a[str(n)] * 17**a[str(o)]
                                    #print("number i  j  k  l  m  n  o")
                                    flist.append([y,x])
    newlist = flist[:]
    newlist.sort()
    # for i in flist:
    #     for j in flist:
    #         if i[0] < j[0]:
    #             continue
    #         else:
    #             if i[0] == j[0]:
    #                 if int(i[1]) < int(j[1]):
    #                     continue
    #                 else:

    print(flist)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(newlist)
    print(len(newlist))

    print("Time taken : ",time.time() - start)
if __name__ == '__main__':
    main()


