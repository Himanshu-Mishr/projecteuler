#---------------------------------------------------#
#     Title: problem 36                             #           
#    Author: Himanshu Mishra                        #
#     email: himanshu.m786@gmail.com                #
#-__________________________________________________#
import time 
"""
About the Program :-
problem 36 of project euler
"""
def main():
	start = time.time()
	sum = 0
	for i in range(1,1000000):
		part_1 = list(str(i))
		part_2 = list(str(i))
		part_2.reverse()
		if part_1[:] == part_2[:]:
			bin_part = bin(i)
			bin_1 = list(bin_part[2:])
			bin_2 = list(bin_part[2:])
			bin_2.reverse()
			if bin_1[:] == bin_2[:]:
				sum += i
				print(i,bin_part,sum)
	print("time taken is ",time.time() - start)
	return 0
if __name__ == '__main__':
	main()	