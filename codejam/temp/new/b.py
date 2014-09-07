import time

def main():
    start = time.time()
    case = int(input())
    for n in range(case):
        opt = [int(r) for r in (input().split(" "))]
        a, b, k = opt[0], opt[1], opt[2]
        count = 0
        c = []
        for i in range(a):
            for j in range(b):
                temp = i&j
                c.append(temp)
                if temp < k:
                    count += 1
        header = "Case #" + str(n+1) + ":"
        print(header, (a, b, k), count, "||", sorted(c))
    print("time taken : ", time.time() - start)
if __name__ == '__main__':
    main()

