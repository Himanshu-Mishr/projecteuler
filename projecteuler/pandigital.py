#-----------------------------------------------------------#
#     Title: pandigital generator                           #
#    Author: Himanshu Mishra                                #
#     email: himanshu.m786@gmail.com                        #
#-----------------------------------------------------------#

import time
def pan():
  start = time.time()
  for i in range(123456789,987654322):
    i_str = str(i)
    alist = list(i_str)
    if len(alist) == len(set(alist)) and ('0' not in alist):
      print(i)

  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  pan()
