#only the dummy example
primes = [2, 3, 5, 7, 11, 13, 17, 19] #listing out all of the primes from 1-20
j = range(2, 20)
a = {} #min
b = {} #max
for i in primes:
	a[i] = 0
	b[i] = 0

for x in j:
	if x in primes:
		b[x] = b[x] + 1
		if b[x] > a[x]:
			a[x] = b[x]
			b[x] = 0
	else:
		temp = x
		i = 0
		while i < len(primes) and temp != 1:
			if temp % primes[i] == 0:
				b[primes[i]] =  b[primes[i]] + 1
				temp = temp/primes[i]
			else:
				i = i+1
		print b
		for i in b:
			if a[i] < b[i]:
				a[i] = b[i]
			b[i] = 0
N = 1
for i in primes:
	if a[i] < b[i]:
		a[i] = b[i]
		N = N * i**a[i]
	else: 
		N = N * i**a[i]

print b
print a
print N



