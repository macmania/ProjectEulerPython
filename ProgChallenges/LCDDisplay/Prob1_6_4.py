#LCD Display problem solution 

#temporary test file 
def drawLCDNum(inputNum, output): 
	#to-do stub
	for y in display:

	return 0

f = open("test1")
lines = f.read().splitlines()
finalOutput = []
for inputNum in lines: 
	arrCommands = inputNum.split(' ')
	size = int(arrCommands[0])	
	displayTemp = list(arrCommands[1]) #splits the number into characters, better processing
	sizeNumbers = len(displayTemp)
	outputArr = [[0 for x in range((size+2)*sizeNumbers)] for y in range((size*2+3)*sizeNumbers)]
	outputArr = drawLCDNum(displayTemp, outputArr) #populates the outputArray
print finalOutput