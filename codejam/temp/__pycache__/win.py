# this is for matching the pattern 

def wining(x_case,o_case):

	win_pattern = [
	[0,1,2,3],
	[4,5,6,7],
	[8,9,10,11],
	[12,13,14,15],
	[[0],[4],[8],[12]],
	[[1],[5],[9],[13]],
	[[2],[6],[10],[14]],
	[[3],[7],[11],[15]],
	[[0],[5],[10],[15]],
	[[3],[6],[9],[12]]	]
	output = "undefined"
	
	for i in win_pattern:
		if i in x_case:
			print("x wins")
		elif i in o_case:
			print("o wins")
	return output

if __name__ == '__main__':
	wining()