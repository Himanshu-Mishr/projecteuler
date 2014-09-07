#---------------------------------------------------#
#     Title: problem 30                             #           
#    Author: Himanshu Mishra                        #
#     email: himanshu.m786@gmail.com                #
#-__________________________________________________#
import time
"""
About the Program :-
problem 30 of project euler
"""
def str_mani(word):
	to_str = str(word)
	word_part =  list(to_str)
	sum = 0
	for i in word_part:
		sum = sum + int(i)**5

	return sum

def main():
	start = time.time()
	sum = 0
	for i in range(200000):
		maniuplated = str_mani(i)
		if maniuplated == i and i != 0 and i != 1:
			print(i)
			sum += i

	print("sum is ",sum)
	print("time taken ",time.time() - start)
	return 0
if __name__ == '__main__':
	main()