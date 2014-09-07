#-------------------------------------------------#
#     Title: problem 60                  roblem 60#           
#    Author: Himanshu Mishra                      #
#     email: himanshu.m786@gmail.com              #
#-------------------------------------------------#
import time
import data_problem60
import prime_data
primeList = prime_data.a
def PrimeChecker(NumberString):
  y = int(NumberString)
  if y in primeList:
    return 1
  else:
    return 0
  return 0
  # x= y//2
  # while x>1:
  #   if y%x == 0:
  #     break
  #   x -= 1
  # else:
  #   return 1
  # return 0

def main():
  start = time.time()    
  two_combination_list = []
  alist = data_problem60.a
  # alist contain all the prime required 
  # now we have to make prime of 5 pair and that too non repeatitative
  # this i is the number that we are going to chat.
  count = 0
  for i in alist:
    print(i)
    i_str = str(i)
    count += 1
    # this j will be going front and back to check it
    #print("--------------------checking ",i)
    for j in alist[count-1:]:
      go_flag_for_y = 0
      success_flag = 0
      #print("--------branch ",j)
      j_str = str(j)
      #front
      x = PrimeChecker(j_str+i_str)
      if (x):
        #print("front is prime")
        go_flag_for_y = 1

      else:
        go_flag_for_y = 0
        success_flag = 0
        #print("1st : failed front")
      if go_flag_for_y == 1:
        y = PrimeChecker(i_str+j_str)
        if (y):
          success_flag = 1
          #print("back is prime")
        else:
          success_flag = 0
          #print("2nd : failed second")
      if(success_flag == 1):
        #print(" works",i,j)
        two_combination_list.append([i,j])
  print(two_combination_list)
  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
