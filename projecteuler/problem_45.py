def main():
	t = set()
	p = set()
	h = set()
	filt1 = set()
	filt2 = set()
	for i in range(100000):
		tri = (i * (i+1 ))/2
		penta = (i*(3*i-1))/2
		hexa = (i*(2*i-1))
		t.add(tri)
		p.add(penta)
		h.add(hexa)

	filt1 = t & p
	filt2 = filt1 & h
	print(filt1)
	print("************************************************************")
	print(filt2)

	return 0

if __name__ == '__main__':
	main()