#------------------------------------------------------------------#
#     Title: checking binary_and_pali.py                  hecking binary_and_pali.py#           
#    Author: Himanshu Mishra                                       #
#     email: himanshu.m786@gmail.com                               #
#------------------------------------------------------------------#
import time
import binary_and_pali
def main():
  start = time.time() 
  # read the file
  f = open("testing.txt",'r')
  noOfCase_temp = f.readline()
  noOfCase = noOfCase_temp.rstrip()
  for i in range(int(noOfCase)):
    word_with_newline = f.readline()
    word = word_with_newline.rstrip()
    alist = word.split(' ')
    a = alist[0] 
    b = alist[1]
    binary_and_pali.main(int(a),int(b))   
  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
