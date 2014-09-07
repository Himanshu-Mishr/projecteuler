#-----------------------------------------------------------#
#     Title: step 2 of problem 60                  tep 2 of problem 60#           
#    Author: Himanshu Mishra                                #
#     email: himanshu.m786@gmail.com                        #
#-----------------------------------------------------------#
import time
import data2
def main():
  start = time.time()    
  alist = data2.a
  count = 0
  for i in alist:
    print("(x,y) = ",i)
    x = i[0]
    y = i[1]
    count += 1
    count1 = 0
    for j in alist[count-1:]:
      a = j[0]
      b = j[1]
      n1 = [x,a]
      n2 = [x,b]
      n3 = [y,a]
      n4 = [y,b]
      # count1 += 1
      # for k in alist[count1-1:]:
      #   p = k[0]
      #   q = k[1]
      #   n5 = [x,p]
      #   n6 = [x,q]
      #   n7 = [y,p]
      #   n8 = [y,q]
      #   n9 = [a,p]
      #   n10= [a,q]
      #   n11= [b,p]
      #   n12= [b,q]
      if (n1 in alist) and (n2 in alist) and (n3 in alist) and (n4 in alist):# and (n6 in alist) and (n8 in alist) and (n10 in alist) and (n12 in alist):# and (n5 in alist) and (n7 in alist) and (n9 in alist) and (n11 in alist):
        print("found this is pair of 4 = ",x,y,a,b)

  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
