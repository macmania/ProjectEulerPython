
#Trick here is to decrement the 
i = 1
n = n_init = 1000
end = 100
listNums = range(201, 21+1)
maxNum = 0

for x in range(900, 1000+1):
	n = x
	while(n > 1):
		if n % 2 == 0: 
			n = n >> 1 #same as n/2
		else: 
			n = 3*n + 1
		i = i + 1
		if maxNum < i:
			maxNum = i
	i = 1

print end, n_init, maxNum