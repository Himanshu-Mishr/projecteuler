#---------------------------------------------------#
#     Title: problem 49                             #           
#    Author: Himanshu Mishra                        #
#     email: himanshu.m786@gmail.com                #
#-__________________________________________________#

"""
About the Program :-
this problem 49 of profect euler
"""


def counter(simi):
	listo = simi
	for i in listo:
		counting = 0
		for j in listo:
			if i == j:
				counting = counting + 1

		if counting >= 2:
			print("++++++++++++++++>>>>>>",counting)

	return True

def consecutive(packet):
	data  = packet
	simi = []
	for i in data:
		for j in data:
			show = int(i)-int(j)
			if show > 0:
				simi.append(show)
				print(show)
	simi.sort()
	count = counter(simi)
#	print("*****************>",simi)

	return True,count




def main():
	line = open("data.txt",'r')

	while line:
		for i in line:
			first = i.rstrip()
			packet = []
			list_first = list(first)
			first_set = set(list_first)
			if len(first_set) == 4:
				print('==========================================>',first)
				for j in open('data.txt','r'):
					second = j.rstrip()
					list_sec = list(second)
					sec_set = set(list_sec)
					if first_set.issubset(sec_set):
						print("------------->",second)
						packet.append(second)

				transfer = consecutive(packet)
				print(transfer)
			next(line)



	return 0
if __name__ == '__main__':
	main()