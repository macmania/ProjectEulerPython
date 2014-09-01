#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#we can see that the 6th prime is 13.
#What is the 10 001st prime number

primes = []
i = 2
isPrime = True
sumPrimes = 0
while len(primes) <= 2000000:
	for x in primes: 
		if i % x == 0:
			isPrime = False
			break

	if isPrime:
		primes.append(i)
	isPrime = True

	i = i + 1

for x in primes: 
	sumPrimes += x

print sumPrimes
