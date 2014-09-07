#----------------------------------------------------------------------#
#     Title: problem A of codeforce.com #210                  roblem A of codeforce.com #210#           
#    Author: Himanshu Mishra                                           #
#     email: himanshu.m786@gmail.com                                   #
#----------------------------------------------------------------------#
import itertools
def main():
  s = input()
  temp = s.split(" ")
  n = int(temp[0])
  k = int(temp[1])
  answer = []
  row_possible = []
  # making list of possible elements
  element_list = []
  for i in range(k+1):
    element_list.append(i)
  # finding all possible sum of k keeping in mind n
  sum_list = itertools.product(element_list,repeat=n)
  for i in sum_list:
    sum  = 0
    for j in i:
      sum += j
    if sum == k:
      # collecting them 
      row_possible.append(i)
  # now finding all possible matrix
  matx_temp = itertools.permutations(row_possible,n)
  # now we have to check for the summation of column
  for i in matx_temp:  
    index = 0
    flag = 0
    while (index<n):
      sum = 0
      for j in i:
        sum += j[index]
      index += 1
      if sum == k:
        flag = 1
        continue
      else:
        flag = 0
        break
    if flag == 1:
      answer.append(i)
  #printing it in matrix form
  for i in answer[1]:
    line = ""
    for j in i:
      line += str(j)
      line += " "
    print(line)
  #print(answer[1])
  return 0
if __name__ == '__main__':
  main()
