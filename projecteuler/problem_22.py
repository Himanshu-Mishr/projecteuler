#---------------------------------------------------#
#     Title: problem 22                             #           
#    Author: Himanshu Mishra                        #
#     email: himanshu.m786@gmail.com                #
#-__________________________________________________#
import time
"""
About the Program :-
problem 22 of project euler 
"""

def main():
	start = time.time()
	f = open("names.txt","r")
	word = f.readline()
	word_list = word.split(",")

	
	total = 0	
	sort_list1 = [] 
	for i in word_list:
		stage1 = i[:-1]
		ready_word = stage1[1:]
		sort_list1.append(ready_word)

	sort_list1.sort()

	for j in sort_list1:
		parted_word = list(j)
		sum = 0
		for k in parted_word:
			sum = sum + (ord(k) - 64)

		score = (sort_list1.index(j) + 1) * sum

		total += score
	

	print("total is ",total)
	end = time.time()
	print("Time taken is = ",end - start)
	return 0
if __name__ == '__main__':
	main()