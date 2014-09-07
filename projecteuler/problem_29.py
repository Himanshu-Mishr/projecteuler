#---------------------------------------------------#
#     Title: problem 29                             #           
#    Author: Himanshu Mishra                        #
#     email: himanshu.m786@gmail.com                #
#-__________________________________________________#
import time
"""
About the Program :-
problem 29 of project euler
"""

def main():
	start = time.time()
	data = []
	for i in range(2,101):
		for j in range(2,101):
			data.append(i**j)

	s = set(data)
	print(len(s))	
	print("time taken ",time.time() - start)	
	return 0
if __name__ == '__main__':
	main()