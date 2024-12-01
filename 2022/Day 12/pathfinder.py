from colorama import Fore

class Node:
	def __init__(self, _walkable, _position):
		self.walkable = _walkable
		self.position = _position
		self.gCost = 0
		self.hCost = 0
		self.parent = None

	def fCost(self):
		return self.gCost + self.hCost

class Pathfinder:
	def __init__(self, _grid, _allowDiagonal, _step = False) -> None:
		self.path = []
		self.allowDiagonal = _allowDiagonal
		self.step = _step
		if type(_grid) == list:
			self.grid = self.stringsToNodes(_grid)
		elif type(_grid) == tuple:
			rows = _grid[0]
			columns = _grid[1]
			self.grid = [[Node(True, (row, column)) for column in range(columns)] for row in range(rows)]

	def stringsToNodes(self, _grid, wallChar = "#"):
		for row in range(len(_grid)):
			for column in range(len(_grid[0])):
				if _grid[row][column] == wallChar:
					_grid[row][column] = Node(False, (row, column))
				else:
					_grid[row][column] = Node(True, (row, column))
		return _grid



	def getNeighbours(self, pos):
		if type(pos) == Node:
			pos = pos.position
		
		if self.allowDiagonal:
			positions = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1), (pos[0] + 1, pos[1] + 1), (pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] - 1), (pos[0] - 1, pos[1] - 1)]
		else:
			positions = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
		toPop = []
		for p in positions:
			if p[0] < 0 or p[1] < 0:
				toPop.append(p)
				continue
			if p[0] >= len(self.grid) or p[1] >= len(self.grid[0]):
				toPop.append(p)
				continue
		for pop in toPop:
			positions.remove(pop)

		neighbours = [self.grid[x][y] for x, y in positions]
		return neighbours
			
	def overrideGrid(self, grid):
		self.grid = self.stringsToNodes(grid)
	
	def getDistance(self, nodeA, nodeB):	#
		x1, y1 = nodeA.position				# Get
		x2, y2 = nodeB.position				# Manhattan
											# Distance
		return abs(x1 - x2) + abs(y1 - y2)	#

	def drawGrid(self, path = [], walkableChar = "■ ", unwalkableChar = "■ ", pathChar = "■ ", edgeChar = "+ ", currentNode = Node(False, (-1, -1))):
		rows = len(self.grid[0])
		columns = len(self.grid)
		
		if not path:
			path = self.path

		print(edgeChar * (rows+2))
		for row in range(columns):
			print(edgeChar, end="")
			for column in range(rows):
				if (row, column) == currentNode.position:
					print(Fore.GREEN + pathChar + Fore.WHITE, end="")
				elif self.grid[column][row] in self.path:
					print(Fore.RED + pathChar + Fore.WHITE, end="")
				elif self.grid[column][row].walkable:
					print(walkableChar, end="")
				else:
					print(Fore.BLACK + unwalkableChar + Fore.WHITE, end="")
			print(edgeChar)
		print(edgeChar * (rows+2))

	def findPath(self, startPos, targetPos):
		startNode = self.grid[startPos[0]][startPos[1]]
		targetNode = self.grid[targetPos[0]][targetPos[1]]

		openSet = [startNode]
		closedSet = []

		while len(openSet) > 0:
			currentNode = openSet[0]
			for i in range(len(openSet)):
				if (openSet[i].fCost() > currentNode.fCost() or openSet[i].fCost() == currentNode.fCost()) and openSet[i].hCost < currentNode.hCost :
					currentNode = openSet[i]

			openSet.remove(currentNode)
			closedSet.append(currentNode)

			if currentNode == targetNode:
				self.path = self.retracePath(startNode, targetNode)
				return

			for neighbourNode in self.getNeighbours(currentNode):
				if (not neighbourNode.walkable) or (neighbourNode in closedSet):
					continue

				newMovementCostToNeighbour = currentNode.gCost + self.getDistance(currentNode, neighbourNode)
				if newMovementCostToNeighbour < neighbourNode.gCost or neighbourNode not in openSet:
					neighbourNode.gCost = newMovementCostToNeighbour
					neighbourNode.hCost = self.getDistance(neighbourNode, targetNode)
					neighbourNode.parent = currentNode

					if not neighbourNode in openSet:
						openSet.append(neighbourNode)
			
			if self.step:
				self.retracePath(startNode, currentNode)
				yield currentNode
		print("No solution found!")
				
	def retracePath(self, startNode, endNode):
		path = []
		currentNode = endNode

		while currentNode.position != startNode.position:
			path.append(currentNode)
			currentNode = currentNode.parent
		path.append(startNode)

		path = path[::-1]	# reverse list (python moment)
		return path
