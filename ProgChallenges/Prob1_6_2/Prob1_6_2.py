import time
#test algorithm first
arr = [[0 for x in range(5)]for x in range(3)]
f = open('test2', 'r')
str_temp = f.read().splitlines()
for x in range(len(arr)):
	char_temp = list(str_temp[x])
	print x
	for y in range(len(arr[x])):
		if char_temp[y] == '*':
			arr[x][y] = '*'
			if x - 1 != -1:
				if arr[x-1][y] != '*':
					arr[x-1][y] += 1
				if y-1 != -1 and arr[x-1][y-1] != '*': 
					arr[x-1][y-1] += 1
				if y+1 != len(arr) and arr[x-1][y+1] != '*':
					arr[x-1][y+1] += 1
			if y - 1 != -1:
				if arr[x][y-1] != '*':
					arr[x][y-1] += 1
				if x + 1 != len(arr) and arr[x+1][y-1] != '*':
					arr[x+1][y-1] += 1
			if x + 1 != len(arr):
				if arr[x+1][y] != '*':
					arr[x+1][y] += 1
				if y + 1 != len(arr[x]) and arr[x+1][y+1] != '*':
					arr[x+1][y+1] += 1
			if y + 1 != len(arr[x]) and arr[x][y+1] != '*':
				arr[x][y+1] += 1
	print arr
	#time.sleep(5)

for x in range(len(arr)):
	print arr[x]








