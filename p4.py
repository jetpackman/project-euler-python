def palindrome_check(n):
	temp = n
	rev = 0
	while temp != 0:
		rev = rev * 10 + temp % 10
		temp = temp // 10

	
	if rev == n:
		return True
max = 0
for i in range(100, 1000):
	for j in range (100,1000):
		if palindrome_check(i * j) and i * j > max:
			max = i * j

print max
