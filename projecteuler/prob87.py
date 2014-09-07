#------------------------------------------------#
#     Title: problem87                  roblem87#           
#    Author: Himanshu Mishra                     #
#     email: himanshu.m786@gmail.com             #
#------------------------------------------------#
import time
import prime_prob87

def main():
  start = time.time()
  alist = prime_prob87.a   
  print(alist)
  asetlist = []
  for i in alist:
    for j in alist:
      for k in alist:
        x = i**2 + j**3 + k**4 
        if ( x < 50000000):
          asetlist.append(x)
  aset = set(asetlist)
  print(len(aset))
  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
