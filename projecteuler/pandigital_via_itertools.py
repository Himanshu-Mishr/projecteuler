#-----------------------------------------------------------#
#     Title: pandigital prime set                           #           
#    Author: Himanshu Mishra                                #
#     email: himanshu.m786@gmail.com                        #
#-----------------------------------------------------------#
import time
import itertools
def main():
  start = time.time()
  evenList = ['2','4','6','8']    
  a = itertools.permutations('123456789')
  for i in a:
    if i[8] not in evenList:
      print(i,",")
        
  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
