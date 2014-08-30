#still doesn't work
import time
#Trick here is to decrement the 
#3n+1 problem 
start_time = time.time()
i = 1
n = n_init = 1000
end = 100
maxNum = 1

for x in range(1, 1000000):
	n = x
	while(n != 1):
		if n % 2 == 0: 
			n = n >> 1 #same as n/2
		else: 
			n = 3*n + 1
		i = i + 1
		if maxNum < i:
			maxNum = i
	i = 1
print maxNum, time.time() - start_time