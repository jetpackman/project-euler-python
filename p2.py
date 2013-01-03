
def makeFibList():
	x = [1,2]
	while x[-1] + x[-2] < 4000000:
		x.append(x[-1] + x[-2])

	print sum ([i for i in x if i % 2 == 0])


makeFibList()
