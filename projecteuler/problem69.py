#-------------------------------------------------#
#     Title: problem 69                  roblem 69#           
#    Author: Himanshu Mishra                      #
#     email: himanshu.m786@gmail.com              #
#-------------------------------------------------#
import time
import fractions
def main():
  start = time.time()    
  max  = 0
  max_n = 0
  for i in range(1,100000):
    count = 0
    for j in range(1,i+1):
      if fractions.gcd(i,j) == 1:
        count += 1
    temp = float(i)/count

    if temp > max:
      max = temp
      max_n = i
  print("for n = ",max_n,"we have maximum n/φ(n) = ",max)
  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
