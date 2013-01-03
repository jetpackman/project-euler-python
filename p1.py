x = range(1,1000)
sum = 0

for num in x:
	if num % 5 == 0 or num % 3 == 0:
		print num
		sum += num

print sum
