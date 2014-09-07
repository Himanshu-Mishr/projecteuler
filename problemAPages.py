"""
Purpose : A. page problem
"""


def main():
    # input
    b = input().split(' ')
    n,p,k = int(b[0]), int(b[1]), int(b[2])

    x = left(n, p, k)
    y = middle(p)
    z = right(n, p, k)

    print(x+y+z)

# left string
def left(n, p, k):
    counter = p-1
    astring = ""
    while counter > 0 and k > 0:
        astring = str(counter) + " " + astring
        counter -= 1
        k -= 1
    if counter != 0:
        astring = "<< " + astring
    return astring

# middle string
def middle(page):
    return '('+str(page)+')'

# right string
def right(n, p, k):
    counter = p+1
    astring = ""
    while counter < n+1 and k > 0:
        astring = astring + " " + str(counter)
        counter += 1
        k -= 1
    if counter != n+1:
        astring = astring + " >>"
    return astring

if __name__ == '__main__':
    main()
