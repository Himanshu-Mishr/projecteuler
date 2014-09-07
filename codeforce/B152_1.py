"""
Domain Name : Codeforces.com
Link        : http://codeforces.com/problemset/problem/158/B
Problem Name: B. Taxi
Method      : greedy, implementation
Coder       : Himanshu-Mishr(himanshu.m786@gmail.com)
"""
#import time
def main():
    #start = time.time()
    n = input()
    atext = input()
    group = [int(i) for i in atext.split(' ')]
    count1, count2, count3, count4, taxi = 0, 0, 0, 0, 0
    for i in group:
        if i == 4:
            count4 += 1
        elif i == 3:
            count3 += 1
        elif i == 2:
            count2 += 1
        elif i == 1:
            count1 += 1
    #print("Pipe : count1 count2 count3 count4 taxi")
    #print("pipe : ",count1, "    ", count2, "    ", count3, "    ", count4, "    ", taxi)
    # for 4
    taxi += count4
    count4 -= count4

    #print("for 4: ",count1, "    ", count2, "    ", count3, "    ", count4, "    ", taxi)

    # for 3
    if count3 > 0:
        if count3 >= count1 :
            count1 -= count1
            taxi += count3
            count3 -= count3

        elif count3 < count1 :
            count1 -= count3
            taxi += count3
            count3 -= count3

    #print("for 3: ",count1, "    ", count2, "    ", count3, "    ", count4, "    ", taxi)

    # for 2
    if count2 > 0:
        if count2%2 != 0: #odd
            #print("debugging : count2 here should be odd",count2)
            if count2 > 1:
                taxi += int((count2-1)/2)
                count2 = 1
        else:
            #print("debugging : count2 here should be even",count2)
            taxi += int(count2/2)  #even
            count2 -= count2

    #print("for 2: ",count1, "    ", count2, "    ", count3, "    ", count4, "    ", taxi)

    # for 2 and 1
    if count2 > 0:
        if count1 <= 2:
            taxi += 1
            count1 -= count1
            count2 -= count2
        if count1 > 2:
            taxi += 1
            count1 -= 2
            count2 -= count2

    #print("for21: ",count1, "    ", count2, "    ", count3, "    ", count4, "    ", taxi)
    # for 1
    if count1 > 0:
        p = int(count1/4)
        if p < 0:
            taxi += 1
        elif count1 %4 == 0:
            taxi += p
        else:
            taxi += (p + 1)

    #print("for 1: ",count1, "    ", count2, "    ", count3, "    ", count4, "    ", taxi)
    print(taxi)
    #print("Time taken : ", time.time() - start)
if __name__ == '__main__':
    main()
