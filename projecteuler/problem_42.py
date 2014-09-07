#---------------------------------------------------#
#     Title: problem 42                             #           
#    Author: Himanshu Mishra                        #
#     email: himanshu.m786@gmail.com                #
#-__________________________________________________#
import time
"""
About the Program :-
problem 42 of project euler 
"""

def main():
	start = time.time()
	f = open("words.txt","r")
	word = f.readline()
	word_list = word.split(",")
	tri_list = []
	for r in range(1,50):
		num = (1/2 )* r* (r + 1)
		tri_list.append(int(num))

	counter = 0
#	print(tri_list)	
	for i in word_list:
		stage1 = i[:-1]
		ready_word = stage1[1:]
		parted_word = list(ready_word)
		sum = 0
		for j in parted_word:
			sum = sum + (ord(j) - 64)

		if sum in tri_list:
			counter = counter + 1
#			print("yes this is",sum)
#		print(sum)

	print("total triangle words are ",counter)
	end = time.time()
	print("Time taken is = ",end - start)
	return 0
if __name__ == '__main__':
	main()