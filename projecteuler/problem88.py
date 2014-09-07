#-------------------------------------------------#
#     Title: problem 88                  roblem 88#           
#    Author: Himanshu Mishra                      #
#     email: himanshu.m786@gmail.com              #
#-------------------------------------------------#
import time
import itertools
def main():
  start = time.time()
  # making a list    
  for i in range(2,16):
    alist = []
    for j in range(1,i+1):
      alist.append(j)
    # find sum and product of each of item in list  
    a = itertools.combinations_with_replacement(alist,i)
    print("  ",i,"--------------")
    temp = []
    for p in a:
      sumOfItem = 0
      productOfItem = 1
      for q in p:
        sumOfItem += q
        productOfItem = productOfItem * q
      if sumOfItem == productOfItem:
        # need take out minimal from it
        temp.append(sumOfItem)
    temp.sort()
    b = temp[0]
    print("  ",i," --> ",b)
  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
