#-------------------------------------------------#
#     Title: problem 89                  roblem 89#           
#    Author: Himanshu Mishra                      #
#     email: himanshu.m786@gmail.com              #
#-------------------------------------------------#
import time

value_dict = {'I':1,
              'V':5,
              'X':10,
              'L':50,
              'C':100,
              'D':500,
              'M':1000}
adict = {1:1,2:2,3:3,4:2,5:1,6:2,7:3,8:4,9:2}

def roman_generator(numList):
  total_sum = 0
  for i in numList:
    x = list(str(i))
    sum = 0
    y = len(x)
    for j in x:
      if (y == 4) and (j == x[0]) and (j == '4'):sum += 4
      elif j == '1':sum += 1
      elif j == '2':sum += 2
      elif j == '3':sum += 3
      elif j == '4':sum += 2   
      elif j == '5':sum += 1
      elif j == '6':sum += 2
      elif j == '7':sum += 3
      elif j == '8':sum += 4
      elif j == '9':sum += 2
      #else:
        #print("###############error######################",i,j)
      #print("--->  ",i,sum)
    total_sum += sum
  print("Minimal characters = ",total_sum)
  return 0

def roman_evalutor(alist):
  numList = []
  for i in alist:
    input_split = list(i)
    sum = 0
    for i in input_split:
      sum += value_dict[i]
    #print(sum)
    numList.append(sum)
  roman_generator(numList)
  return 0

# this function juct proccess the file and gets the data from it.
def main():
  start = time.time()
  normal_sum = 0
  # proccessing the file    
  f = open("roman.txt",'r')
  alist = []
  for i in f:
    a = i.rstrip()
    alist.append(a)

  roman_evalutor(alist)

  g = open("a2.txt",'r')
  for i in g:
    b = i.rstrip()
    normal_sum += len(b)
  print("Given characters = ",normal_sum)
  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
