import operator
b = input().split(' ')
x, y = int(b[0]), int(b[1])
print(operator.xor(x,y))
