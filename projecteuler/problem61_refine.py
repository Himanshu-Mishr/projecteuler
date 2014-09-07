#--------------------------------------------------------#
#     Title: problem 61 refine                  roblem 61 refine#           
#    Author: Himanshu Mishra                             #
#     email: himanshu.m786@gmail.com                     #
#--------------------------------------------------------#
import time
import refine_output
import data_prob61

tri = data_prob61.tri
sqr = data_prob61.sqr
penta = data_prob61.penta
hexa = data_prob61.hexa
hepta = data_prob61.hepta
octa = data_prob61.octa
def main():
  start = time.time()    
  a = refine_output.a
  for i in a:
    print("--------------")
    print(i)
    count = 0
    for j in i:
      if(j == 'tri'):
        if(i['sqr'] not in tri) and (i['penta'] not in tri) and (i['hexa'] not in tri) and (i['hepta'] not in tri) and (i['octa'] not in tri):
          count += 1
          print("tri check OK",count)
        else:print("tri failed")
      if(j == 'sqr'):
        if(i['tri'] not in sqr) and (i['penta'] not in sqr) and (i['hexa'] not in sqr) and (i['hepta'] not in sqr) and (i['octa'] not in sqr):
          count += 1
          print("sqr check OK",count)
        else:print("sqr failed")
      if(j == 'penta'):
        if(i['tri'] not in penta) and (i['sqr'] not in penta) and (i['hexa'] not in penta) and (i['hepta'] not in penta) and (i['octa'] not in penta):
          count += 1
          print("penta check OK",count)
        else:print("penta failed")
      if(j == 'hexa'):
        if(i['tri'] not in hexa) and (i['sqr'] not in hexa) and (i['penta'] not in hexa) and (i['hepta'] not in hexa) and (i['octa'] not in hexa):
          count += 1
          print("hexa check OK",count)
        else:print("hexa failed")
      if(j == 'hepta'):
        if(i['tri'] not in hepta) and (i['sqr'] not in hepta) and (i['penta'] not in hepta) and (i['hexa'] not in hepta) and (i['octa'] not in hepta):
          count += 1
          print("hepta check OK",count)
        else:print("hepta failed")
      if(j == 'octa'):
        if(i['tri'] not in octa) and (i['sqr'] not in octa) and (i['penta'] not in octa) and (i['hexa'] not in octa) and (i['hepta'] not in octa):
          count += 1
          print("octa check OK",count)
        else:print("Octa failed")
      if count == 6:
        print("this is the answer ",i)

  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
