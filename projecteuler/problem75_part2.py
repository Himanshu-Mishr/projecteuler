#-----------------------------------------------------#
#     Title: problem part 2                           #           
#    Author: Himanshu Mishra                          #
#     email: himanshu.m786@gmail.com                  #
#-----------------------------------------------------#
import time
import temp1
def main():
  start = time.time()    
  a = temp1.a
  b = temp1.b
  c = temp1.c
  d  = temp1.d
  e  = temp1.e
  f  = temp1.f 
  g  = temp1.g 
  h  = temp1.h
  i  = temp1.i
  j  = temp1.j 
  k  = temp1.k 
  l  = temp1.l
  m  = temp1.m  

  total_count = 0
  counter = 0
  print("########### a ")
  for x in a:
    counter = a.count(x)
    if counter <= 1:
      total_count += 1
      print(" --> ",total_count,x)
    # else:
    #   continue

  counter = 0
  print("########### b ")  
  for x in b:
    counter = b.count(x)
    if counter <= 1:
      total_count += 1
      print(" --> ",total_count,x)
    # else:
    #   continue
  
  counter = 0
  print("########### c  ")
  for x in c:
    counter = c.count(x)
    if counter <= 1:
      total_count += 1
      print(" --> ",total_count,x)
    # else:
    #   continue
  
  counter = 0
  print("########### d ")
  for x in d:
    counter = d.count(x)
    if counter <= 1:
      total_count += 1
      print(" --> ",total_count,x)
    # else:
    #   continue
  
  counter = 0
  print("########### e ")
  for x in e:
    counter = e.count(x)
    if counter <= 1:
      total_count += 1
      print(" --> ",total_count,x)
    # else:
    #   continue
  
  counter = 0
  print("########### f ")
  for x in f:
    counter = f.count(x)
    if counter <= 1:
      total_count += 1
      print(" --> ",total_count,x)
    # else:
    #   continue
  
  counter = 0  
  print("########### g ")
  for x in g:
    counter = g.count(x)
    if counter <= 1:
      total_count += 1
      print(" --> ",total_count,x)
    # else:
    #   continue
  
  counter = 0
  print("########### h ")
  for x in h:
    counter = h.count(x)
    if counter <= 1:
      total_count += 1
      print(" --> ",total_count,x)
    # else:
    #   continue
  
  counter = 0
  print("########### i ")
  for x in i:
    counter = i.count(x)
    if counter <= 1:
      total_count += 1
      print(" --> ",total_count,x)
    # else:
    #   continue
  
  counter = 0
  print("########### j ")
  for x in j:
    counter = j.count(x)
    if counter <= 1:
      total_count += 1
      print(" --> ",total_count,x)
    # else:
    #   continue
  
  counter = 0
  print("########### k ")
  for x in k:
    counter = k.count(x)
    if counter <= 1:
      total_count += 1
      print(" --> ",total_count,x)
    # else:
    #   continue
  
  counter = 0
  print("########### l ")
  for x in l:
    counter = l.count(x)
    if counter <= 1:
      total_count += 1
      print(" --> ",total_count,x)
    # else:
    #   continue
  
  counter = 0
  print("########### m ")
  for x in m:
    counter = m.count(x)
    if counter <= 1:
      total_count += 1
      print(" --> ",total_count,x)
    # else:
    #   continue
  print("Answer = ",total_count)
  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
