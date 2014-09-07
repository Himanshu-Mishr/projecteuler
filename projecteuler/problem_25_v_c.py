def main():
	old_number = 1
	current_number = 1
	print(1)
	while 1:
		print(current_number)
		next_number = current_number + old_number
		old_number = current_number
		current_number = next_number
		if (len(str(current_number)) > 1001):
			print(current_number)
			break
			
	return 0

	
if __name__ == '__main__':
	main()