#-------------------------------------------------#
#     Title: problem104                  roblem104#           
#    Author: Himanshu Mishra                      #
#     email: himanshu.m786@gmail.com              #
#-------------------------------------------------#
import time
import data_problem104
a = data_problem104.a
def main():
  start = time.time()    
  counter = 0
  for i in a:
    first_word = i[0]
    last_word = i[1]
    if(len(list(first_word)) == len(set(list(first_word))) and len(list(last_word)) == len(set(list(last_word)))):# and '0'not in first_word and '0' not in last_word):
      print(counter)


  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
