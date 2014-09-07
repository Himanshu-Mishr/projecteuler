#-------------------------------------------------#
#     Title: problem118                           #           
#    Author: Himanshu Mishra                      #
#     email: himanshu.m786@gmail.com              #
#-------------------------------------------------#
import time
import problem118_data
a = problem118_data.a
def main():
  count = 0
  start = time.time()    
  for i in a:
    for j in a:
      if(i != j):
        for k in a:
          if(k != j and k != i and len(i+j+k) < 10 and len(list(i+j+k)) == len(set(list(i+j+k)))):
            for l in a:
              if(len(i+j+k) > 9):break
              if(l != k and l != j and l != i and len(i+j+k+l) < 10):
                for m in a:
                  if(len(i+j+k+m) > 9):break
                  if( m != k and m != l and m != j  and m != i and len(i+j+k+l+m) < 10 and len(list(i+j+k+l+m)) == len(set(list(i+j+k+l+m)))):
                    for n in a:
                      if(len(i+j+k+m+n) > 9):break
                      if (n != m and n != k and n != l and n != j  and n != i and len(i+j+k+l+m+n) < 10):
                        for o in a:
                          if(len(i+j+k+m+n+o) > 9):break
                          #print(" i am HERE",len(i+j+k+m+n+o)," |||| ",i,j,k,l,m,n,o,i+j+k+l+m+n+o,)
                          if(o  != n and o != m and o != k and o != l and o != j  and o != i and len(i+j+k+l+m+n+o) == 9 and len(list(i+j+k+l+m+n+o)) == len(set(list(i+j+k+l+m+n+o)))):
                            print(i,j,k,l,m,n,o,i+j+k+l+m+n+o,len(i+j+k+l+m+n+o))
                            count += 1

  
  
  print("Answer is = ",count)
  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
