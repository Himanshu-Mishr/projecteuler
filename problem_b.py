"""
Purpose : B. Red and Blue Balls
"""

def main():
    n = int(input())
    s = list(input())
    steps = 0
    #print("----------")
    while True:
        #print(steps)
        #printStack(s)
        if "B" in s:
            steps += 1
            if s[0] == "R":
                s = redPop(s)
            if s[0] == "B" or s == []:
                s = blueReplaceRed(s)
                s = fillStack(s, n)
        else:
            break

    print(steps)

def redPop(s):
    pos = s.index("B")
    if pos == 0:
        s = []
    else:
        s = s[pos:]
    return s

def blueReplaceRed(s):
    s = ["R"] + s[1:]
    return s

def fillStack(s, n):
    if len(s) == n:
        return s
    else:
        diff = n - len(s)
        while diff > 0:
            s = ["B"] + s
            diff -= 1
    return s

def printStack(s):
    astring = ""
    for i in s:
        astring += i
    #print(astring)

if __name__ == '__main__':
    main()
