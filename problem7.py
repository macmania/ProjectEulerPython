#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#we can see that the 6th prime is 13.
#What is the 10 001st prime number

primes = []
i = 2
isPrime = True
while len(primes) <= 10001 and i < 10000000:
	for x in primes: 
		if i % x == 0:
			isPrime = False
			break

	if isPrime:
		primes.append(i)
	isPrime = True

	i = i + 1

print primes[10000]
print len(primes)