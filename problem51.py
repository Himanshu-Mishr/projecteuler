import time
def main():
    start = time.time()

    # selecting odd
    z = ['1', '3', '7', '9']
    canBePrime = [ i for i in range(1, 100000, 2) if str(i)[-1] in z]

    # making primes
    prime = []
    for i in canBePrime:
        x = i//2
        while x>1:
            if i%x == 0:break
            x -= 1
        else:prime.append(i)
    print(prime)

    print("Time taken : ",time.time() - start)

if __name__ == '__main__':
    main()
