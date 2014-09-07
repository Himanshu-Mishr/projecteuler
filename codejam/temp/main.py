
import palindrome

def main(a,b,j):
	data = open("C-large-attempt0.out",'a') #output file
	counter1 = palindrome.palindrome_and_sqrt(a,b)
	my_string = "Case #%d: %d\n"%(j,counter1)
	data.write(my_string)
	data.close()
	return counter1
if __name__ == '__main__':
	main()