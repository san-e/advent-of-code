import string
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

letters = string.ascii_lowercase
letterValues = {"S": 0, "E": 25}
for i, letter in enumerate(letters):
    letterValues[letter] = i + 1

with open("input.txt", "r") as f:
    input = [list(l) for l in f.read().split("\n")]
for row, _ in enumerate(input):
    for column, letter in enumerate(_):
        input[row][column] = letterValues[letter]



grid = Grid(matrix = input, width=len(input[0])-1, height=len(input)-1)

start = grid.node(0, 20)
end = grid.node(44, 20)

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
path, runs = finder.find_path(start, end, grid)
print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end, show_weight=True))