#-------------------------------------------------#
#     Title: problem 61                  roblem 61#           
#    Author: Himanshu Mishra                      #
#     email: himanshu.m786@gmail.com              #
#-------------------------------------------------#
import time
import data_prob61
import itertools

tri = data_prob61.tri
sqr = data_prob61.sqr
penta = data_prob61.penta
hexa = data_prob61.hexa
hepta = data_prob61.hepta
octa = data_prob61.octa
whole = [tri,sqr,penta,hexa,hepta,octa]


def cyclic_checker(alist1,alist2,alist3,alist4,alist5,alist6):
  z = {'1081':"tri",'1089':"sqr",'1080':"penta",'1128':"hexa",'1177':"hepta",'1160':"octa"}
  for i in alist1:
    first_part_tri = i[:2]
    last_part_tri = i[2:]
    for j in alist2:
      first_part_sqr = j[:2]
      if last_part_tri == first_part_sqr:
        #print(i," --> ",j)
        last_part_sqr = j[2:]
        for k in alist3:
          first_part_penta = k[:2]
          if last_part_sqr == first_part_penta:
            #print(i," ---> ",j," ---> ",k)
            last_part_penta = k[2:]
            for l in alist4:
              first_part_hexa = l[:2]
              if last_part_penta == first_part_hexa:
                #print(i," ---> ",j," ---> ",k," ---> ",l)
                last_part_hexa = l[2:]
                for m in alist5:
                  first_part_hepta = m[:2]
                  if last_part_hexa == first_part_hepta:
                    #print(i," ---> ",j," ---> ",k," ---> ",l," ---> ",m)
                    last_part_hepta = m[2:]
                    for n in alist6:
                      first_part_octa = n[:2]
                      last_part_octa = n[2:]
                      if last_part_hepta == first_part_octa and last_part_octa == first_part_tri:
                        #print("-----------------------------------------")
                        print(i," ---> ",j," ---> ",k," ---> ",l," ---> ",m," ---> ",n)
                        #print (z[alist1[1]]," ---> ",z[alist2[1]]," ---> ",z[alist3[1]]," ---> ",z[alist4[1]]," ---> ",z[alist5[1]]," ---> ",z[alist6[1]])
                        #newlist = [i,j,k,l,m,n]
                        #newlist.sort()
                        #print("sorted list = ",newlist)
                        #print(z[alist1[1]],':',i,',',z[alist2[1]],':',j,',',z[alist3[1]],':',k,',',z[alist4[1]],':',l,',',z[alist5[1]],':',m,',',z[alist6[1]],':',n," sum =  ",int(i)+int(j)+int(k)+int(l)+int(m)+int(n))
                        #print(int(i)+int(j)+int(k)+int(l)+int(m)+int(n))

def main():
  start = time.time()
  a = itertools.permutations(whole)
  for i in a:
    cyclic_checker(i[0], i[1], i[2], i[3], i[4], i[5])
  print("Time Taken is = ",time.time()-start)
  return 0
if __name__ == '__main__':
  main()
