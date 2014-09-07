#-------------------------------------------------#
#     Title: problem 59                           #
#    Author: Himanshu Mishra                      #
#     email: himanshu.m786@gmail.com              #
#-------------------------------------------------#
import time
import operator
import itertools
def unlock(mylist,encrptedData):
  # copy
  for x in mylist:
    print(x[0])
    p = x[0]
    q = x[1]
    r = x[2]
    word = ''
    temp = encrptedData[:]
    #print(temp)
  # pop
    while temp:
      #print(p,q,r)
      temporary_popped_char = temp.pop(0)
      #print(temporary_popped_char)
      xor_key = p
      char1 = chr(operator.xor(ord(temporary_popped_char[0]),p))
      # if char1 not in ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
      #   word = ''
      #   break
      word += char1
      p = q
      q = r
      r = xor_key

    print("word is here ",word)
    print(" -----------------------------------------------------------------")
  return 0

adict = {'a':97,
        'b':98,
        'c':99,
        'd':100,
        'e':101,
        'f':102,
        'g':103,
        'h':104,
        'i':105,
        'j':106,
        'k':107,
        'l':108,
        'm':109,
        'n':110,
        'o':111,
        'p':112,
        'q':113,
        'r':114,
        's':115,
        't':116,
        'u':117,
        'v':118,
        'w':119,
        'x':120,
        'y':121,
        'z':122
        }


''' main : connects all '''
def main():
  start = time.time()    
  # creating a list the file
  f = open("cipher1.txt",'r')
  b = f.readline()
  print(b)
  f.close()
  encrptedData = b.split(',')
  strg = 'abcdefghijklmnopqrstwuvxyz'
  a = itertools.product(strg,repeat=3)
  mylist = []
  for i in a:
    temp = [adict[i[0]],adict[i[1]],adict[i[2]]]
    mylist.append(temp)
  #keys list 
  # keyList = []
  # for i in a:
  #   keys = []
  #   for j in i:
  #     keys.append(ord(j))
  #   keyList.append(keys)
  # passing keyList and encrptedData
  unlock(mylist,encrptedData)
  #tryme(encrptedData)
  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
