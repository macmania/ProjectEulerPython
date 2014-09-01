f = open("tests/prob8Test")
tempStr = ''.join(f.read().splitlines())
head, tail  = 0, 0
maxProd, tempProd = 1, 1

while head < len(tempStr) and tail < len(tempStr):
	tail = head + 13
	possProd = tempStr[head:tail]

	zeroLoc = possProd.find('0')
	if zeroLoc != -1: 
		tail = zeroLoc + 1
	else: 
		#print possProd
		tempProd = reduce(lambda x, y: int(x)*int(y), possProd)
	if maxProd < tempProd:
		maxProd = tempProd
	head += 1
print maxProd
