# problem 466
# coder : Himanshu Mishra
import matplotlib.pyplot as plt
def main():
    a = list(range(1, 65))
    c = [] + a
    xAxis = []
    yAxis = []
    for j in range(100):
        temp = 0
        d = c[-4:-1]
        for i in d:
            temp += 1
            c.append(i+temp)
        # print(set(c))
        # print(64, "x", j+1, "=", len(set(c)))
        xAxis.append(j+1)
        yAxis.append(len(set(c)))
    # 1st list is about x-axis
    # 2nd list is about y-axis
    # 3rd agrument is about color and type of marking for the interection
    plt.plot(xAxis,yAxis)
    plt.xlabel(" as column increses ")
    plt.ylabel(" no of distinct element ")
    plt.axis('normal')
    plt.grid()
    plt.show()



if __name__ == '__main__':
    main()
