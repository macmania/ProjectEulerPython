i = 999
j = 999

while ( i > 900):
	while (j > 900):
		x = str(i * j)
		j_ = len(x) - 1
		i_ = 0
		isPalindrome = True 
		while (i_ < j_ and isPalindrome):
			if x[i_] != x[j_]:
				isPalindrome = False
			j_ = j_ - 1
			i_ = i_ + 1
		if isPalindrome:
			print x, i, j
			print isPalindrome
			break
			
		j = j - 1
	i = i - 1
	j = 999

##This tests whether a particular 
##string is a palindrome

print isPalindrome


