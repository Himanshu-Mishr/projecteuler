# this is my  MAIN file

import winner

def readfile():
	f= open("A-large.in",'r') #input file
	first = f.readline()
	loop = first.rstrip()
	looper = int(loop)
	for x in range(looper):  # for each differnet case different loop

		pattern_list = []	# for each diff case diff matrix
		j = 0
		for i in f:	

			right_remove = i.rstrip()       # striping the newline character
			part = list(right_remove) # spliting them using the space 
			pattern_list.append(part)
			j = j + 1
			if j == 4:
				f.readline()
				break

#		print(pattern_list)
		p,output = winner.main(x,pattern_list)
#		print(output)

	return 0

if __name__ == '__main__':
	readfile()