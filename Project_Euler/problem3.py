i = 3
num = 600851475143
while i <= num:
	if num % i == 0: 
		num = num/i
		print num
		print i
	i += 2

print i
print num
