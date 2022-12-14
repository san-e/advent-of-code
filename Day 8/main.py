with open("Day 8/input.txt", "r") as f:
	input = f.read().split("\n")

def all_(iterable):
	for element in iterable:
		index = element[1]
		if not element[0]:
			return [False, index]
	try:
		return [True, index]
	except:
		return [True, 1]

def solve():
	global row
	global column
	nOfVisibleTrees = 0
	highestScenicScore = 0
	for row, numbers in enumerate(input):
		numbers = numbers.rstrip("\n")
		for column, number in enumerate(numbers):				# disregard tree if at the edge
			if 	column == 0 or column == len(input[0]) - 1 \
				or row == 0 or row == len(input) -1:			#
				nOfVisibleTrees += 1							#
				continue										#


			try:
				up, upIndex = all_([input[row-i][column] < number, i] for i in range(1, row + 1))
				down, downIndex = all_([input[row+i][column] < number, i] for i in range(1, len(input) - (row + 1)))
				left, leftIndex = all_([input[row][column-i] < number, i] for i in range(1, column + 1))
				right, rightIndex = all_([input[row][column+i] < number, i] for i in range(1, len(input[0]) - (column)))
				if up or down or left or right:
					nOfVisibleTrees += 1
			except IndexError:
				nOfVisibleTrees += 1
			
			scenicScore = upIndex * downIndex * leftIndex * rightIndex
			if scenicScore > highestScenicScore: highestScenicScore = scenicScore
				
	return 	nOfVisibleTrees, highestScenicScore

answer = solve()
print(f"Answer 1: {answer[0]}\nAnswer 2: {answer[1]}")