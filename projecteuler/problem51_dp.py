#------------------------------------------------#
#     Title: problem51                  roblem51#           
#    Author: Himanshu Mishra                     #
#     email: himanshu.m786@gmail.com             #
#------------------------------------------------#
import time
import itertools
import prime_numbers_list
primeList = prime_numbers_list.a

def main():
  start = time.time()    
  last_part = ['1','7']
  # calculate how much to replace
  for i in range(2,5):
    a = itertools.product('0123456789',repeat=i)
    for j in a:
      for k in last_part:
        temp = list(j) + [k]
        #print("------------------------------------------++++++")
        #print(">>check",temp)
        for p in range(len(temp)-1): 
          for s in range(len(temp)-1):
            #for t in range(len(temp)-1):
              #print("Index = ",p,s)#,t)
              count = 0
              for q in range(10): 
                if p != s:
                  temp[p] = str(q)
                  temp[s] = str(q)
                #temp[t] = str(q)  
                else:temp[s] = str(q)               
                req_str = ''
                for r in temp:req_str += r
                #print(req_str)
                if(int(req_str) in primeList):
                  count += 1
                  #print("string ",req_str,"-->> ",count)
                
              if count >= 7 :
                print(temp,"--------->> ",count,"--index",p,s)#,t)

  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
    # printing the combination ready to be replaced
    #                
    #                |
    #         ______\|/_____
    #         |            |
    #         |      x     |
    #         |____________|
    #                |
    #               \|/
    # 
    #   x = to be replaced 
    #   Remember : last element has to be 1,3,7,9
    
