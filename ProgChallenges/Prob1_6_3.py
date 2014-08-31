#The trip UVA/PC problem

f = open("test1.1_6")
lines = iter(f.read().splitlines())
#start = next(lines)
x = next(lines)

while x != '0' and  x != 0:  
	try: 
		x = int(x)
	except: 
		break
	if isinstance(x, int): 
		y = [0 for z in range(x)]
		i = 0
		exp = float(next(lines))

		sumExp = 0
		while isinstance(exp, float) and exp != 0 and i < x: 
			y[i] = float(exp)
			exp = float(next(lines))
			sumExp += y[i]
			i += 1
		expDiv = round(sumExp/len(y), 2)
		posDif, negDif = 0, 0 
		for j in y: 
			temp = expDiv - j
			if temp < 0:
				negDif += temp
			else:
				posDif += temp
		print '${0:.2f}'.format(negDif) if ((negDif * -1) < posDif) else '${0:.2f}'.format(posDif)
		#print posDif
		y = []
	x = exp
	
