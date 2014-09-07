import time
def main():
    #------------------------------------------------
    # input
    t = input()
    in_data = []
    for i in range(int(t)):
        in_data.append(int(input()))

    #------------------------------------------------
    # performing required operation
    start = time.time()
    for i in in_data:
        sum = 0
        for j in range(1,int((i/2)+2)):
            if (i%j)==0:sum+=j
        sum +=i

    #------------------------------------------------
    # output
        print(sum)
    print("Time Taken = ",time.time() - start)
    return 0

if __name__ == '__main__':
    main()