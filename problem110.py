for i in range(1000000000000, 10000000000, -1):
    # print("total> ", i)
    n = (i)*(i-1)
    for j in range(i, int((2/3)*i), -1):
        # print("blue> ", j)
        d = (j)*(j-1)
        if d*2 == n:
            print(j)
