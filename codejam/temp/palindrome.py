import math
import check_pali

def palindrome_and_sqrt(a,b):
	mylist = []
	newlist = []
	for i in range(a,b):
		part1 = list(str(i))
		part2 = list(str(i))
		part2.reverse()
		if part1[0:] == part2[0:]:
    			mylist.append(i)

	for j in mylist:
		root = math.sqrt(j)
		if int(root + 0.5) ** 2 == j:
			newlist.append(int(root))


	
	counter = check_pali.main(newlist)

	return counter

if __name__ == '__main__':
	palindrome_and_sqrt()