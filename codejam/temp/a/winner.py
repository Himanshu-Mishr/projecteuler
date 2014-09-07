def main(j,pat):
	dot = '.'
	output = []
	choice = ['T','T']
	kela = ["X","O"]
	for le in kela:
		i = 0
		choice[0] = le
		print(choice)

		if(
		(pat[0][0] in choice and pat[0][1] in choice and pat[0][2] in choice and pat[0][3] in choice) or
		(pat[1][0] in choice and pat[1][1] in choice and pat[1][2] in choice and pat[1][3] in choice) or
		(pat[2][0] in choice and pat[2][1] in choice and pat[2][2] in choice and pat[2][3] in choice) or
		(pat[3][0] in choice and pat[3][1] in choice and pat[3][2] in choice and pat[3][3] in choice) or
		(pat[0][0] in choice and pat[1][0] in choice and pat[2][0] in choice and pat[3][0] in choice) or
		(pat[0][1] in choice and pat[1][1] in choice and pat[2][1] in choice and pat[3][1] in choice) or
		(pat[0][2] in choice and pat[1][2] in choice and pat[2][2] in choice and pat[3][2] in choice) or
		(pat[0][3] in choice and pat[1][3] in choice and pat[2][3] in choice and pat[3][3] in choice) or
		(pat[0][0] in choice and pat[1][1] in choice and pat[2][2] in choice and pat[3][3] in choice) or
		(pat[0][3] in choice and pat[1][2] in choice and pat[2][1] in choice and pat[3][0] in choice)):
			output.append(le + ' won')


		else:
			if (
			(pat[0][0] == dot and pat[0][1] == dot and pat[0][2] == dot and pat[0][3] == dot) or
		(pat[1][0] == dot and pat[1][1] == dot and pat[1][2] == dot and pat[1][3] == dot) or
		(pat[2][0] == dot and pat[2][1] == dot and pat[2][2] == dot and pat[2][3] == dot) or
		(pat[3][0] == dot and pat[3][1] == dot and pat[3][2] == dot and pat[3][3] == dot) or
		(pat[0][0] == dot and pat[1][0] == dot and pat[2][0] == dot and pat[3][0] == dot) or
		(pat[0][1] == dot and pat[1][1] == dot and pat[2][1] == dot and pat[3][1] == dot) or
		(pat[0][2] == dot and pat[1][2] == dot and pat[2][2] == dot and pat[3][2] == dot) or
		(pat[0][3] == dot and pat[1][3] == dot and pat[2][3] == dot and pat[3][3] == dot)
		): output.append("Game has not completed")

			else : output.append("Draw")

		i += 1

	print(pat)
	for z in range(4):
		no_dot = len([k for k, x in enumerate(pat[z]) if x == "."])
	print(no_dot)


	if "won" in output[0]:
		outer = output[0]
	elif "won" in output[1]:
		outer = output[1]
	elif no_dot >= 1:
		outer = "Game has not completed"
	else:
		outer = "Draw"

	data = open("A-large-1.out",'a') #output file
	my_string = "Case #%d: %s\n"%(j+1,outer)
	data.write(my_string)
	data.close()
	return j,outer

if __name__ == '__main__':
	main()
