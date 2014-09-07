
for i in range(10000000,100000000):
    iStr = str(i)
    x = '1' + iStr[0] + '2' + iStr[1] +'3' + iStr[2] + '4' + iStr[3] + '5' + iStr[4] + '6' + iStr[5] + '7' + iStr[6] + '8' + iStr[7] + '9' + '0' + '0'
    if i == int(x)**1/2:
        print("ANSWER : ",i)

