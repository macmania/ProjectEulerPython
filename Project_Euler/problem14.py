#still doesn't work
import time
#Trick here is to decrement the 
#3n+1 problem 
#need to be optimized

def nextN(i):
	if (i & 1):
		return i * 3 + 1
	return i >> 1

start_time = time.time()
i = 1
n = n_init = 1000
end = 100
maxNum = 1
#1000000
cache = {k: 0 for k in range(2,1000000)}

for x in range(2, 1000000):
	n = long(x)
	
	while(n != 1):
		if n < len(cache) and cache[x] != 0: 
			break
		n = nextN(n)
		i = i + 1
	if i == 525: 
		print x
		break
	if maxNum < i:
		maxNum = i
	cache[x] = i
	i = 1

print maxNum, time.time() - start_time