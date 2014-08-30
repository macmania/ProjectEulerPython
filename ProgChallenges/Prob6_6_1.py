#count range of fibonacci sequences between x and y such that 
# 0<x<y<10^100

a = 1
b = 2

#temporary dummies
init_ = 1234567890
end_ = 9876543210
i = 0
#starting fibonacci sequence
while (b <= end_):
	b = a + b
	a = b
	if b >= init_: 
		i += 1
print i
