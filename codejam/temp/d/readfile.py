import pattern

def main():

	f = open("D-small-attempt0.in",'r')
	first = f.readline()
	case_str = first.rstrip()
	case_no = int(case_str)
	for i in range(case_no):
		# for each case
		second = f.readline()
		sec_str = second.rstrip()
		part = sec_str.split(' ')
		loop_no = int(part[1])
		door = []
		third = f.readline()
		th_str = third.rstrip()
		key_types = th_str.split(' ')
		for j in range(loop_no):
			
			temp = f.readline()
			temp_str = temp.rstrip()
			door.append(temp_str.split())

		print(key_types,door)
		ouptut = pattern.main(key_types,door)
		print(ouptut)

	return 0

if __name__ == '__main__':
	main()