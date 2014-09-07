import main

def readfile():
	f= open("C-large-1.in",'r') #input file
	first = f.readline()
	loop = first.rstrip()
	looper = int(loop)
	j = 0
	for i in f:
		j = j + 1
		right_remove = i.rstrip()       # striping the newline character
		part = right_remove.split(' ') # spliting them using the space 
		a,b = int(part[0]),int(part[1])
		main.main(a,b+1,int(j))

		if j == looper:
			break

	return 0

if __name__ == '__main__':
	readfile()