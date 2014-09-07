import itertools
import time

z=0
a=1
b=2
c=5
d=10
e=20
f=50
g=100
h=200

#def rollercoster(log,picecs)
#  a = itertools.combinations_with_replacement(log,picecs)
#  for i in a:
#    print(i)
#  return

def main():
  start = time.time()
  #creating the log
  # we have create tuple for that
  data_list = [z,a,b,c,d,e,f,g,h]
  data = [0,1,2,3,4,5,6,7,8]
  x = itertools.product(data,repeat=3)
  p = [(a, b, c) for (a,b,c) in x if a+b+c == 8]
  count = 0
  for i in p:
    count += 1
    print(i,' ==== ',count)

  print("Total time taken = ",time.time() - start)
  return 0
if __name__ == '__main__':
  main()
