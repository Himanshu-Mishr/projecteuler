import problem15
x = problem15.a
sum = 0
max = 0
def main():
    s = recur(0, 0)
    print("exhausted = ",s)
    print("MAX > ", max)


def recur(p, q):
    global sum, max
    print(p, q)
    if p>13 or q>13:
        return 0
    sum += x[p][q]
    recur(p+1, q)
    if sum > max:
        max = sum
    print(" ------ > ", sum)
    sum = 0
    recur(p+1, q+1)
if __name__ == '__main__':
    main()

