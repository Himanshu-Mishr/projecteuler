x = [2,6,20,70,252,924,3432,12870,48620,184756,705432,2704156,10400600,40116600,155117520,601080390,2333606220]
for i in range(len(x)-1):
    print("numerator : %d denominator : %d division : "%(x[i+1], x[i]), x[i+1]/x[i])
