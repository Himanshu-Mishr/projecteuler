#------------------------------------------------------------------------#
#     Title: Binary Number which is palindrome                  inary Number which is palindrome#           
#    Author: Himanshu Mishra                                             #
#     email: himanshu.m786@gmail.com                                     #
#------------------------------------------------------------------------#
def main(InitalNumber,FinalNumber):    
  # taking input from user
  #InitalNumber = int(input("Enter the starting number : "))  # starting number
  #FinalNumber  = int(input("Enter the last number : "))      # ending number
  counter = 0
  # picking out every number from InitialNumber to FinalNumber
  for i in range(InitalNumber,FinalNumber+1):           
    # this convert a number to binary, but it is in string format  '0bxxxxxxxx'
    temp = bin(i)
    # binary number should not start with 0
    if temp[3] != '0':                      
      # we are slicing & removing '0b' from temp
      word1 = list(temp[2:])             
      # we will reverse another copy of the binary 
      # and then we will check each other for equality
      word2 = list(temp[2:])
      word2.reverse()   
      if word1[0:] == word2[0:]:
        counter += 1
  if counter == 0:
    print("none")
  else:
    print(counter)
  return 0
if __name__ == '__main__':
  main()
