# coder : Himanshu Mishra (himanshu.m786@gmail.com)
# program : 101

def main():
    for i in range(1, 21):
        n = i
        x = 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
        print(n, ">",x)
if __name__ == '__main__':
    main()
