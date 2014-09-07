import time
# main parameters 
# data.txt ---  contain the prime number from 1000 to 10000

def main():
	start = time.time()
#--------------------------------------------------------------------------------------------#
	# open the file for reading purpose only 
	# and saving the file object to f1
	f = open("data.txt",'r')
	prime_list = []
	#right stripping the '\n' element  
	for i in f:       
		# saving every thing in a list for use 
		# means making data ready 
		prime_list.append(i.rstrip())

	#
	#creating a list with permutation sequence 
	#
	prime_permu = []
	for p in range(len(prime_list)):
		
		temp = [] #
				  #	creating a tempo list so that we can add at the end of the loop to the main
				  # list that is prime_permu 
				  # 
		for q in range(p,len(prime_list)):
			
			# sorting them and comparing 
			a = sorted(list(prime_list[p]))
			b = sorted(list(prime_list[q]))
			if a[0] == b[0] and a[1] == b[1] and a[2] == b[2] and a[3] == b[3]:
			#	print(prime_list[p],prime_list[q])
				temp.append(prime_list[q])

		prime_permu.append(temp)

	#
	# At the end of this line we will get the a list which contain strings.
	# Now we have to find the difference between 
	#
	
	#print(prime_permu)
	# 
	# len(prime_permu) will give length of whole list 
	# len(prime_permu[r]) will give the length of the nested list
	#  len(prime_permu[r][s]) will select each elemt of the nested list  
	#  
	
	for r in range(len(prime_permu)):                       #  [...................lenght..............................]
		#print("----------------------------")
		diff = []
		for s in range(len(prime_permu[r])):                #  [..[a,b,c,d........lenght.......].[.........lenght...........].]  and taking out letters one by one 
			
			for t in range(1,len(prime_permu[r])):          #   [...[a,b,c,d,e,f,g,h,i,..........]...[...........].....]

				if not (int(prime_permu[r][s]) == int(prime_permu[r][t])):
					diff = abs(int(prime_permu[r][s]) - int(prime_permu[r][t]))
					if diff == 3330:
						print(prime_permu[r][s])

#----------------------------------------------------------------------------------------------#
	end = time.time()
	print(end-start)
	return 0


if __name__ == '__main__':
		main()