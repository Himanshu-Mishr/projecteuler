# coder : Himanshu Mishra (himanshu.m786@gmail.com)
# program : Problem 118

import mathTools
import time
def pan():
  start = time.time()
  for i in range(123456789,987654322):
    i_str = str(i)
    alist = list(i_str)
    if len(alist) == len(set(alist)) and ('0' not in alist):
        block = breakInBlock(i)
        if checkBlockPrime(block):
            print(i)
  print("Time Taken is = ",time.time()-start)
  return 0

def breakInBlock(i):

    return block

def checkBlockPrime(block):
    for i in block:
        for j in i:
            if mathTools.checkPrime(j):
                ...
            else: break
    else:
        return
    return false

if __name__ == '__main__':
  pan()
