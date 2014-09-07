"""
Purpose : problem 206
Coder   : Himanshu Mishra (himanshu.m786@gmail.com)
"""


def problem206():
    for i in range(1000000000, 10000000000, 10):
        #print(i)
        x = str(i**2)
        xlist = [x[-19], x[-17], x[-15], x[-13], x[-11], x[-9], x[-7], x[-5], x[-3], x[-0]]
        #y = str(i)
        #ylist = [x[-2], x[-4], x[-6], x[-8], x[-10], x[-12], x[-14], x[-16], x[-18]]
        req = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if xlist[:] == req[:]: #and ylist[:] == list(y):
            print("____________>", i)
if __name__ == '__main__':
    problem206()
