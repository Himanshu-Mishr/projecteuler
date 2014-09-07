#-------------------------------------------------#
#     Title: problem112                  roblem112#           
#    Author: Himanshu Mishra                      #
#     email: himanshu.m786@gmail.com              #
#-------------------------------------------------#
import time

def main():
  start = time.time()
  count_normal = 0
  count = 0    
  for i in range(100,50000):
    count_normal += 1
    i_str = str(i)
    for j in range(int(len(i_str)/2)):
      if (i_str[j] > i_str[j+1]) and (i_str[j+2] > i_str[j+1]):
        print(i)
        count += 1
  print("percentage ---> ",(count/count_normal)*100)

  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
