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
def divisor_sum(number):
	sum = 0
	for i in range(1,number):
		if number%i == 0:
			sum += i
	return sum

def main():
	count = 0
	start = time.time()
	for i in range(1,10000):
		sum = divisor_sum(i)
		if sum < 10000:
			back_sum = divisor_sum(sum)
			if i == back_sum and sum != back_sum:
				print(sum,back_sum)
				count = count + sum
	print('total sum is ', count)
	print("time taken is  ",time.time() - start)
	return 0
if __name__ == '__main__':
	main()