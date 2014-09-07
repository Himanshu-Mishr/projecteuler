
def main(mylist):
	newlist = []
	counter = 0
	print(mylist)
	for i in mylist:
		part1 = list(str(i))
		part2 = list(str(i))
		part2.reverse()
		if part1[0:] == part2[0:]:
    			newlist.append(i)
    			counter = counter + 1




	return counter

if __name__ == '__main__':
	main()