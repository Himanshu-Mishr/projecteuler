# problem 65
import time

def main():
    start = time.time()
    alist = [2]
    for i in range(1,34):
        alist.append(1);alist.append(2*i);alist.append(1)
    #print(len(alist))

    count = 0
    x2 = alist[0]
    count += 1
    #print(count, "-> ", x2)
    x3 = alist[1]*alist[0] + 1
    count += 1
    #print(count, "-> ", x3)

    for i in alist[2:]:
        temp = x3
        x3 = i*x3 + x2
        x2 = temp
        count += 1
        #print(count, "-> ", x3)
    astr = str(x3)
    sum = 0
    print("100th NUMBER", astr)
    for i in astr:
        sum += int(i)
    print("SUM = ", sum)
    print("Time taken : ", time.time() - start)
if __name__ == '__main__':
    main()
