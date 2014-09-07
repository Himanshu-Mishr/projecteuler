def main():
	old_number = 1
	current_number = 1
	print(1)
	while 1:
		print(current_number)
		next_number = current_number + old_number
		old_number = current_number
		current_number = next_number
		z = str(current_number)
		num1 = len(z)
		print(num1)
		if (num1 >= 1000):
			print(current_number)
			break
			
	return 0


if __name__ == '__main__':
	main()