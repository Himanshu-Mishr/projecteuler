#---------------------------------------------------#
#     Title: problem 36                             #           
#    Author: Himanshu Mishra                        #
#     email: himanshu.m786@gmail.com                #
#-__________________________________________________#

"""
About the Program :-
problem 36 of project euler
"""

def main():
	for i in range(1000):
		part_1 = list(str(i))
		part_2 = part_1.reverse()
		if part_1 == part_2:
			print(part_1)

	return 0
if __name__ == '__main__':
	main()	