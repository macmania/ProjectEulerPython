while (1):
	userInput = raw_input("")
	n,r = long(userInput.split(" ")[0]), long(userInput.split(" ")[1])
	ans = [] 

	k = n >> 1 if n % 2 == 0 else (n-1) >> 1
	k -=1
	i, val, tempVal = 0, 0, 0
	r -= 1

	if(2*r + 1 <= n):
		print 2*r + 1
	else: 
		if n == r+1:
			print 2*(k+1)
		elif n != 1 and n == r:
			print 2 
		elif n == 1: 
			print 1
		else:
			print ((r - k)*2)


'''while (i != r and 2*val + 1 <= n):
	#ans.append((val << 1) + 1) 
	tempVal = (val << 1) + 1
	i += 1 
	val += 1


val = 1

while(i != r and 2*val <= n):
	tempVal = val << 1
	i += 1
	val += 1'''

#print tempVal
	


