
n = int(input())
for i in range(n):
    a = (input().split(" "))
    a.reverse()
    print("Case #",i+1,": ",sep='', end='')
    for j in a:
        print(j, end=' ')
    print()
