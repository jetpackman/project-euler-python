n = 1
while True:
	print n
	works = True
	for i in range (2, 21):
		if n % i != 0:
			works = False
		if works == False:
			break
	if (works == True):
		print n
		break;
	n+=1

