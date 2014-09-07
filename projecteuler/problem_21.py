#---------------------------------------------------#
#     Title: problem 21                             #           
#    Author: Himanshu Mishra                        #
#     email: himanshu.m786@gmail.com                #
#-__________________________________________________#
import time
"""
About the Program :-
problem 21 of project euler
"""

def main():
	start = time.time()
	sum_list = []

	######################################
	for i in range(1,10000):
		divisors = []
		sum = 0
		for j in range(1,i):
			if i%j == 0:
				sum += j 
				divisors.append(j)
	
		sum_list.append(sum)
	#	print('input',i,'sum is ',sum)
	######################################
	print(sum_list)
	for r in sum_list:
		#print(r)
		if r < 10000 and (sum_list[r] == sum_list.index(r)):
			print(sum_list.index(r),r) 
	

	#print(sum_list)
	print('time taken is ',time.time() - start)
	return 0
if __name__ == '__main__':
	main()