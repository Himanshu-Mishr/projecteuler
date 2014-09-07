import time
# amount of cases
start = time.time()
n = int(input())
for i in range(n):
    max = 0
    maxX = 0
    maxY = 0
    temp = 0
    # input weight
    weight = int(input())
    # no of  items
    n = int(input())
    # input all item
    val = [int(j) for j in (input().split(" "))]
    for p in range(len(val)):
        for q in range(len(val)):
            if p != q:  # both item should not be same
                temp = val[p] + val[q]
                if temp <= weight:
                    if temp > max:
                        maxX = p
                        maxY = q
                        max = temp
    # print("Max = ", temp, (maxX+1, maxY+1))
    print("Case #%d:"%(i+1), maxX+1, maxY+1)
print("time taken: ", time.time()-start)
