#---------------------------------------------------#
#     Title: problem 39                             #           
#    Author: Himanshu Mishra                        #
#     email: himanshu.m786@gmail.com                #
#-__________________________________________________#

"""
About the Program :-
problem 39 of project euler
"""
#def checker(i,j,k):
#	a = [i,j,k]
#	a.sort()
#	if (a[0]**2 + a[1]**2) == (a[2]**2):
#		response = True
#	else:
#		response = False

#	return response

def main():
	keys = []
	for i in range(1,1001):
		for j in range(1,1001-i):
			for k in range(1,1001-j-i):
				a = [i,j,k]
				a.sort()
				if (a[0]**2 + a[1]**2) == (a[2]**2):
					sum = i + j + k
					print(i,j,k,"------------  ",sum)
					if sum not in keys:
						keys.append(sum)
						keys.insert(keys.index(sum) + 1,0)

					else:
						keys[keys.index(sum) + 1] = keys[keys.index(sum) + 1] + 1	
				else:
					continue
	print(keys)
	return 0
if __name__ == '__main__':
	main()