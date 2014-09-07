#---------------------------------------------------#
#     Title: problem 26                             #           
#    Author: Himanshu Mishra                        #
#     email: himanshu.m786@gmail.com                #
#-__________________________________________________#

"""
About the Program :-
problem 26 of project euler 
"""
import time
def main():
	start = time.time()
	for i in range(1,1000):
		print(i,1/i)
	print("time taken ",time.time()-start)	
	return 0
if __name__ == '__main__':
	main()