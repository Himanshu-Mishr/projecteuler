import pattern

# this is my  MAIN file

def readfile():
	counting = 0
	f= open("B-large.in",'r') #input file
	first = f.readline()
	loop_str = first.rstrip()
	loop_no = int(loop_str)
	for x in range(loop_no): 				 
	# for each differnet case different loop
	# like case #: 

		
			
		
		# this for loop is to get the index for the matrix	
		# and run that number of times
		for i in f:  						 
			pattern_list = []				    # this has been created for diff cases
			counting += 1
			in_remove = i.rstrip()				# striping the '\n' part
			in_part = in_remove.split(' ')		# spliting and making a list
			
			i_row = int(in_part[0])				# getting the number number of row here in this 
												# in order toget its elements
			i_col = int(in_part[1])
			counter = 1							#counting rows
			for j in f:	
				
				right_remove = j.rstrip()      # striping the newline character
				part = right_remove.split(' ') # spliting them using the space 
				pattern_list.append(part)	   # making a new list of that split
				# and then adding it to same list defined earlier
				
				if counter == i_row:		   # check whether it has exceeded row number
					break
				counter += 1
						
			########################################
			#send the pattern to new file
			#--------------------------------------
			output = pattern.code_lawnmower(i_row,i_col,pattern_list)
			print(output)
			data = open("B-large.out",'a') #output file
			my_string = "Case #%d: %s\n"%(counting,output)
			data.write(my_string)
			data.close()
		
 

	return 0

if __name__ == '__main__':
	readfile()