import time
import data_problem18

count = 0
a = data_problem18.p
sum = 0
max = 0
path = []
def recursion(x, y):
    #print(x, y)
    global sum, path
    path.append([x,y])
    sum += a[x][y]

    if x == 0 or y == 0:
        global count,max
        count += 1
        #print("Sum = ",sum)
        if sum > max:
            max = sum
            print("path ----> ",path)
            print("-----> ",max)
        sum = 0
        path = []

    if x > 0 and y > 0:
        pass
    else:
        path = []
        return "DONE"
    recursion(x-1, y)
    recursion(x, y-1)

def main():
    start = time.time()

    recursion(16, 16)
    global count
    print("Total sum : ",count)

    print("Time taken : ", time.time() - start)
if __name__ == '__main__':
    main()
