b = input().split(' ')
x, y = int(b[0]), int(b[1])
sum = 0
while x < y+1:
    sum += x**2
    x += 1
print(sum)
