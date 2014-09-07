# post no 200
import math
import numbers
def main():
	for i in range(1000):
		a=i*i
		for j in range(1000):
			b=j*j
			c = a + b
			s = math.sqrt(c)
			print i
			print j
			print s
			print "sum = ",i+j+s
			w = isinstance(s, numbers.Integral)
			if w == True:
				print a+b+c 
				

	return 0

if __name__ == '__main__':
	main()
