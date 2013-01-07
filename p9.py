for i in range(3, 1000):
	for j in range(3,1000):
		for k in range(3,1000):
			if (i ** 2 + j**2 == k**2 and i + j + k == 1000 ):
				print str(i) + " "  + str(j) + " " + str(k)


print "finish"
