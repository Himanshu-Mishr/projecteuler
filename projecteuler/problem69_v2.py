#------------------------------------------------#
#     Title: problem69                  roblem69#           
#    Author: Himanshu Mishra                     #
#     email: himanshu.m786@gmail.com             #
#------------------------------------------------#
import time

def dig_out_prime_in_it(ckecklist):
  alist = []
  for y in ckecklist:
    x= y//2
    while x>1:
      if y%x == 0:
#       print(y,"has factor",x)
        break
      x -= 1
    else:
      alist.append(y)
  print(alist)
  return 0

def main():
  start = time.time()    
  for i in range(2,10000):
    checklist = []
    print("\nchecking  ===  ",i)
    for j in range(1,i):
      if(i%j == 0):checklist.append(j)
    dig_out_prime_in_it(checklist)
  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
