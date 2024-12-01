import string
from copy import deepcopy
from pathfinder import Pathfinder
import os

letters = string.ascii_lowercase
letterValues = {"S": 0, "E": 25}
for i, letter in enumerate(letters):
    letterValues[letter] = i + 1

with open("Day 12/input.txt", "r") as f:
    input = [list(l) for l in f.read().split("\n")]

def findIndex(list, toFind):
	for i, sublist in enumerate(list):
		try:
			return (i, sublist.index(toFind))
		except:
			pass

def layerList(list, layer):
	list = deepcopy(list)
	acceptableLayers = (layer - 1, layer, layer + 1)
	for i in range(len(list)):
		for j in range(len(list[0])):
			if list[i][j] not in acceptableLayers:
				list[i][j] = "#"
			else:
				list[i][j] = " "

	return list

startPoint = findIndex(input, "S")
endPoint = findIndex(input, "E")

for row, _ in enumerate(input):
    for column, letter in enumerate(_):
        input[row][column] = letterValues[letter]

rows = len(input)
columns = len(input[0])
layer = 0
layers = {a: layerList(input, a) for a in range(25)}

pathfinder = Pathfinder(_grid = layerList(input, layer), _allowDiagonal = True, _step = True)

for currentNode in pathfinder.findPath(startPoint, endPoint):
	pos = currentNode.position
	for i in range(len(pathfinder.grid)):
		for j in range(len(pathfinder.grid[0])):
			if layers.get(layer)[i][j] == "#":
				pathfinder.grid[i][j].walkable = False
			else:
				pathfinder.grid[i][j].walkable = True
	#pathfinder.drawGrid(currentNode = currentNode)
	layer = input[pos[0]][pos[1]]
	os.system('cls')
	pathfinder.drawGrid(currentNode = currentNode, path = pathfinder.retracePath(pathfinder.grid[startPoint[0]][startPoint[1]], currentNode))