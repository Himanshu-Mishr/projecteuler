# coder : Himanshu Mishra
# Problem D. Deceitful War

def main():

    # no of test cases
    n = int(input())
    for i in range(n):

        # no of wooden block
        item = int(input())

        # naomi
        naomiBucket = [float (j) for j in (input().split(" "))]
        x = naomiBucket[:]
        nx = naomiBucket[:]
        # ken
        kenBucket = [float (j) for j in (input().split(" "))]
        y = kenBucket[:]
        by = kenBucket[:]
        # DECEITFUL WAR
        count = 0
        countSort = 0
        x.sort()
        for j in range(item):
            naomiChoosen = x[j]
            temp = y[:]
            naomiTold = deceitEnemy(temp)
            kenchoosen, y = minimumHigest(naomiTold, y)
            if naomiChoosen > kenchoosen:
                countSort += 1

        countReverse = 0
        x.reverse()
        for j in range(item):
            naomiChoosen = x[j]
            temp = by[:]
            naomiTold = deceitEnemy(temp)
            kenchoosen, by = minimumHigest(naomiTold, by)
            if naomiChoosen > kenchoosen:
                countReverse += 1
        if countReverse > countSort:
            print("Case #%d:"%(i+1),countReverse, end=' ')
        else:
            print("Case #%d:"%(i+1),countSort, end=' ')

        # OPTIMAL WAR
        count = 0
        for j in range(item):
            naomiChoosen = naomiBucket[j]
            kenchoosen, kenBucket = minimumHigest(naomiChoosen, kenBucket)
            if naomiChoosen > kenchoosen:
                count += 1
        print(count)

# returns the minimum highest from the list
def minimumHigest(x, alist):
    templist = []
    for i in alist:
        if i > x:
            templist.append(i)
    templist.sort()
    if len(templist) > 0:
        selected = templist[0]
    else:
        selected = alist[0]
    alist.remove(selected)
    return selected, alist

# fake choosen by naomi
def deceitEnemy(alist):
    alist.sort()
    x = alist[-1]
    return  x - 0.0000001

if __name__ == '__main__':
    main()
