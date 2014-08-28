primes = [2, 3, 5, 7, 11, 13, 17, 19] #listing out all of the primes from 1-20
x = range(2, 20)
factors = {}

for (i in x): 
	for p in primes: 
		if p < i:
			if p % i == 0:  
				smallFactor = p
				i_temp = i/p
				factors[i] = [p]
				while(i_temp > p)

