import time
import data_problem18
a = data_problem18.p
sum = 0
path = []

def recursion(x, y):
    global sum, path

    # controls the recursion
    if x > 0 and y > 0:
        print([x,y], sep=' ', end=' --> ')
    else:
        print("\n\n\n\n")
        return "DONE"
    '''
    path.append([x,y])
    sum += a[x][y]

    if x == 0 or y == 0:
        print("Here")
        print("Path > ",path)
        print("Sum > ",sum)
        sum = 0
        path = []
    '''

    recursion(x-1, y)
    recursion(x, y-1)

def main():
    start = time.time()
    print(recursion(15, 15))
    print("Time taken : ", time.time() - start)
if __name__ == '__main__':
    main()
