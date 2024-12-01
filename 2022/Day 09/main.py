from copy import deepcopy

with open("Day 9/input.txt", "r") as f:
	input = f.read().split("\n")
input = [x.split(" ") for x in input]

def isDiagonalUpperRight(tail, head):
	y1, x1 = head
	y2, x2 = tail
	return 	(y1, x1) == (y2 + 1, x2 - 1)

def isDiagonalUpperLeft(tail, head):
	y1, x1 = head
	y2, x2 = tail
	return 	(y1, x1) == (y2 + 1, x2 + 1)

def isDiagonalLowerRight(tail, head):
	y1, x1 = head
	y2, x2 = tail
	return 	(y1, x1) == (y2 - 1, x2 - 1)

def isDiagonalLowerLeft(tail, head):
	y1, x1 = head
	y2, x2 = tail
	return 	(y1, x1) == (y2 - 1, x2 + 1)

def isAdjacentRight(tail, head):
	y1, x1 = head
	y2, x2 = tail
	return 	(y1, x1) == (y2, x2 - 1)

def isAdjacentLeft(tail, head):
	y1, x1 = head
	y2, x2 = tail
	return 	(y1, x1) == (y2, x2 + 1)

def isAdjacentLower(tail, head):
	y1, x1 = head
	y2, x2 = tail
	return 	(y1, x1) == (y2 - 1, x2)

def isAdjacentUpper(tail, head):
	y1, x1 = head
	y2, x2 = tail
	return 	(y1, x1) == (y2 + 1, x2)


def doMove(move, value):
	global headIndex
	global tailIndex
	global uniquePositions

	match move:
		case "U":
			for i in range(value):
				
				if isDiagonalLowerRight(tailIndex, headIndex): tailIndex = deepcopy(headIndex)
				elif isDiagonalLowerLeft(tailIndex, headIndex): tailIndex = deepcopy(headIndex)
				elif isAdjacentLower(tailIndex, headIndex): tailIndex = deepcopy(headIndex)
				
				uniquePositionsPart1.add(tuple(tailIndex))
				headIndex[0] = headIndex[0] - 1
				

		case "D":
			for i in range(value):
				if isDiagonalUpperRight(tailIndex, headIndex): tailIndex = deepcopy(headIndex)
				elif isDiagonalUpperLeft(tailIndex, headIndex): tailIndex = deepcopy(headIndex)
				elif isAdjacentUpper(tailIndex, headIndex): tailIndex = deepcopy(headIndex)

				uniquePositionsPart1.add(tuple(tailIndex))
				headIndex[0] = headIndex[0] + 1
				

		case "L":
			for i in range(value):
				if isDiagonalLowerRight(tailIndex, headIndex): tailIndex = deepcopy(headIndex)
				elif isDiagonalUpperRight(tailIndex, headIndex): tailIndex = deepcopy(headIndex)
				elif isAdjacentRight(tailIndex, headIndex): tailIndex = deepcopy(headIndex)

				uniquePositionsPart1.add(tuple(tailIndex))
				headIndex[1] = headIndex[1] - 1
				
				

		case "R":
			for i in range(value):
				if isDiagonalLowerLeft(tailIndex, headIndex): tailIndex = deepcopy(headIndex)
				elif isDiagonalUpperLeft(tailIndex, headIndex): tailIndex = deepcopy(headIndex)
				elif isAdjacentLeft(tailIndex, headIndex): tailIndex = deepcopy(headIndex)

				uniquePositionsPart1.add(tuple(tailIndex))
				headIndex[1] = headIndex[1] + 1
				

headIndex = [0, 0]
tailIndex = [0, 0]
nineTailIndex = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
uniquePositionsPart1 = set([tuple(tailIndex)])

for move, value in input:
	doMove(move, int(value))

print(len(uniquePositionsPart1))

