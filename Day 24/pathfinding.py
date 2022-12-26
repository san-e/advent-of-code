class Node:
	walkable: bool
	position: tuple
	gCost: int
	hCost: int

	def __init__(self, _walkable, _position):
		self.walkable = _walkable
		self.position = _position

	def fCost(self):
		return self.gCost + self.hCost


class Pathfinding:
	grid: list(list())

	def __init__(self, _grid: tuple) -> None:
		self.grid = _grid

	def getNeighbours(self, pos):
		positions = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
		toPop = []
		for p in positions:
			if p[0] < 0 or p[1] < 0:
				toPop.append(p)
				continue
			if p[0] > len(self.grid) or p[1] > len(self.grid[0]):
				toPop.append(p)
				continue
		for pop in toPop:
			positions.remove(pop)
		return positions
			
	def getDistance(nodeA, nodeB):
		posA = nodeA.position
		posB = nodeB.position
		dstY = abs(posA[0] - posB[0])
		dstX = abs(posA[1] - posB[1])
		if dstY > dstX:
			dstY, dstX = dstX, dstY
			
		return 10*dstY + 10*dstX	# only do orthogonal movement

	def findPath(self, startPos, targetPos):
		startNode = Node(True, startPos)
		targetNode = Node(True, targetPos)

		open = [startNode]
		closed = []

		while len(open) > 0:
			currentNode = open[0]
			for i in range(1, open + 1):
				if (open[i].fCost() > currentNode.fCost()) or (open[i].fCost() == currentNode.fCost() and open[i].hCost < currentNode.hCost) :
					currentNode = [open[i], i]

				open.pop(currentNode[1])
				closed.append(currentNode[0])

				if currentNode == targetNode:
					return

				for neighbour in self.getNeighbours(currentNode.position):
					if not neighbour.walkable or neighbour in closed:
						continue

				