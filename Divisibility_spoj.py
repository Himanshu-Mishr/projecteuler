t = int(input())
while t > 0:
    b = input().split(' ')
    n, x, y = int(b[0]), int(b[1]), int(b[2])
    t -= 1
    for i in range(2,n):
        if (i%x == 0) and (i%y != 0):
            print(i,end=' ')
    print()
