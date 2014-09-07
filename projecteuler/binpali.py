
def check_pali(InitalNumber,FinalNumber):    
  counter = 0
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
    return "none"
  else:
    return counter

def main():
  noOfCase = input()
  answerList = []
  for i in range(int(noOfCase)):
    word = input()
    alist = word.split(' ')
    a = alist[0] 
    b = alist[1]
    answerList.append(check_pali(int(a),int(b)))

  for i in answerList:
    print(i)
  return 0
if __name__ == '__main__':
  main()
