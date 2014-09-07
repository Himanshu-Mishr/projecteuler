#---------------------------------------------------#
#     Title: problem 21                             #           
#    Author: Himanshu Mishra                        #
#     email: himanshu.m786@gmail.com                #
#-__________________________________________________#

"""
About the Program :-
problem 21 of project euler
"""
import time
def main():
	start = time.time()
	for i in range(1,10000):
		divisors = []
		sum = 0
		for j in range(1,i):
			if i%j == 0:
				sum += j 
				divisors.append(j)
	print("time taken is  ",time.time() - start)
	return 0
if __name__ == '__main__':
	main()