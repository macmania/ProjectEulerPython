userInput = raw_input("")
n,r = int(userInput.split(" ")[0]), int(userInput.split(" ")[1])
ans = [] 

k = n >> 1 if n % 2 == 0 else (n-1) >> 1

i, val = 0, 0

while (i != r and 2*val + 1 <= 2*k+1):
	ans.append((val << 1) + 1) 
	i += 1 
	val += 1
val = 1
while(i != r and 2*val <= 2*k):
	ans.append(val << 1)
	i += 1
	val += 1

print ans[len(ans)-1] if len(ans)-1 > 0 else ans[0]
	