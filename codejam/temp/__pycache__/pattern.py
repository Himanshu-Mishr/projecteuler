# this is for generating the pattern

import win
def pattern(pattern_list):
	my_list = pattern_list
	print(my_list)
	x_case = []
	o_case = []
	for i in range(4):
		x_case.append([k for k, x in enumerate(my_list[i]) if x == "X" or x == "T"])
		o_case.append([j for j, y in enumerate(my_list[i]) if y == 'O' or y == 'T'])
		
		

	print(x_case,o_case)
	output = win.wining(x_case,o_case)
	return output

if __name__ == '__main__':
	pattern()