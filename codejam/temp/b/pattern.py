
# taking input as pat 
# pat => is the input is the pattern
def code_lawnmower(rows,cols,pat):
	pat_int = convert(pat)
	app_pat = []

	#create a mtrix of r x c
	for i in range(rows):
		app_pat.insert(i,[])
		for j in range(cols):
			app_pat[i].insert(j,2)

	for a in range(rows):
		if len(set(pat_int[a])) == 1:
			for b in range(cols):
				if pat_int[a][b] == 1:
					app_pat[a][b] = 1
	

	app_pat_trans = transpose(app_pat)
	pat_int_trans = transpose(pat_int)
	
	print(pat_int)
	print(pat_int_trans)
	print(app_pat)
	
	for p in range(cols):
		if len(set(pat_int_trans[p])) == 1:
			for q in range(rows):
				if pat_int_trans[p][q] == 1:
					app_pat_trans[p][q] = 1

	print(app_pat_trans)
	if app_pat_trans == pat_int_trans:
		output = "YES"
	else:
		output = "NO" 



	# first clear temp will store the slashed number
	

	#print(pat_int)
	#print(temp)

	return output

if __name__ == '__main__':
	code_lawnmower()


# this function will take pattern as input and return the max of it
#def max_pattern(pat_int):
#	# it better to make a copy of it
#	temp = pat_int[:]
#	temp.sort()
#	print(temp)
#	maxy = temp[-1][-1]
#	return maxy

# coverting all the list item to int
def convert(pat):

	pat_int = []   				#this is my main pattern in integer
	for i in pat:
		if type(i) == list:
			temp = []
			for j in i:
				temp.append(int(j))
			pat_int.append(temp)
		else:
			pat_int.append(int(i))
	#print(pat_int)
	return pat_int

# this function is for transpose 
def transpose(matrix):
	b = list(zip(*matrix))
	trans = [list(x) for x in b]
	return trans	