# coder : Himanshu Mishra
# Problem B. Cookie Clicker Alpha

def main():
    n = int(input())
    for i in range(n):
        [c, f, x] = [float (j) for j in (input().split(" "))]
        t = 0.0      # total time
        tc = 0.0     # time for buying cookies farm
        tx = 0.0     # time for buying building
        r = 2.0
        firstbridge = 0.0
        secondbridge = 0.0
        while (True):
            tc = c/r
            tx = x/r
            firstbridge = t + tx
            r = r + f
            tx = x/r
            secondbridge = t + tc + tx
            if firstbridge <= secondbridge:
                print("Case #%d:"%(i+1),firstbridge);
                break
            t = t + tc
if __name__ == '__main__':
    main()
