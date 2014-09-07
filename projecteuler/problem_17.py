#---------------------------------------------------#
#     Title: problem 17                             #           
#    Author: Himanshu Mishra                        #
#     email: himanshu.m786@gmail.com                #
#-__________________________________________________#

"""
About the Program :-
problem 17 of project euler
"""
import time
def main():	
	start =time.time() 
	f = open("problem_17_data.txt",'r')
	counter = 0
	for i in f:
		back_off = i.rstrip()
		count = 0
		for j in back_off:
			if j != ' ':
				count += 1
		counter += count
		#print(back_off,'--',count)
	print("total count is ",counter)
	print("time taken is ",time.time() - start)
	return 0
if __name__ == '__main__':
	main()	