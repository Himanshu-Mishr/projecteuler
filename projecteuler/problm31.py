# using combinations_with_replacement('zx',y)
# z  =  zero
# x  = all combination of (a,b,c,d,e,f,g,h)
# y  = 201 - x_value
# coins = 'abcdefgh'
# xlist = contains all the possible combination of x
import itertools
import time
main_counter = 0
stng_dict = {'z':0,'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
######################################################
#@profile
def number_of_coins(zx,y):
  global main_counter
  global stng_dict
  # this function : runs & proccesses each zx and y using itertools
  # and then we sum each list created by them & check == 200
  start = time.time()
  #combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD
  coins_collection = itertools.combinations_with_replacement(zx,y)
  counter = 0
  for i in coins_collection:
    sum = 0 
    for j in i:
      sum += stng_dict[j]
    if sum == 200:
      counter += 1
  main_counter += counter
  print(" Stng = ",zx," | count = ",counter," | Time = ",time.time() - start," | main_counter = ",main_counter)
  return 0 

######################################################
#@profile
def find_x_value(xlist):
  global stng_dict
  # this function : evaluates the value of each list in xlist
  # and passes zx and y to other function for last evaluation
  for i in xlist:
    #print("list for evaluation = ",i)
    sum = 0
    zx = 'z'
    for j in i:
      zx += j
      sum += stng_dict[j]
    y = 201 - sum
    number_of_coins(zx,y)
  return 0

########################################################  
#@profile
def find_x():
  # this function : finds all possible ways for x
  # returns : x's list as xlist   
  xlist = []
  coins = 'abcdefgh'
  for i in range(1,9):
    # we need only combinnations
    # for further view on what it gives out see the 
    # python docs for itertools -> combinations
    temp = itertools.combinations(coins,i)
    for j in temp:
      xlist.append(list(j))
  return xlist

#########################################################
#@profile
def main():
  # this the main function : it connects all :) 
  start = time.time()
  # 1st finding all possible ways of x
  # find_x should return a list
  xlist = find_x()
  # 2nd running the loop and finding the value of each list of x
  find_x_value(xlist)
  print("TOTAL POSSIBILITIES = ",main_counter)
  print("Total time taken = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()

  