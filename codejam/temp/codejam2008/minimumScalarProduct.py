n = int(input())
for i in range(n):
    n = int(input())
    val1 = [int(j) for j in (input().split(" "))]
    val2 = [int(j) for j in (input().split(" "))]
    val1.sort()
    val2.sort()
    val2.reverse()
    sum = 0
    for p in range(n):
        sum += val1[p]*val2[p]
    print("Case #%d:"%(i+1), sum)
