import time
count = 0
def recursion(x, y):
    print(x, y)
    if x == 0 or y == 0:
        global count
        count += 1

    if x > 0 and y > 0:
        pass
    else:
        return "DONE"
    recursion(x-1, y)

    recursion(x, y-1)

def main():
    start = time.time()
    for i in range(2,3):
        print("-----------------------------------------")
        recursion(i, i)
        global count
        print("Total count for %d : "%i, count)
        print("Time taken for %d  : "%i, time.time() - start)
        count = 0
    print("Time taken : ", time.time() - start)
if __name__ == '__main__':
    main()
