def contains(x, y):
	return any(x == y[i:i + len(x)] for i in range(len(y) - len(x)+1)) # no clue how this works

def overlaps(a, b):
	return any(c in b for c in a)

with open("input.txt", "r") as f:
	input = f.readlines()

input = [[x.split("-") for x in i.rstrip("\n").split(",")] for i in input]

numberOfPairs = 0
numberOfOverlaps = 0
for range0, range1 in input:
	range0 = range(int(range0[0]), int(range0[1]) + 1)
	range1 = range(int(range1[0]), int(range1[1]) + 1)

	if contains(range0, range1) or contains(range1, range0):
		numberOfPairs += 1
	if overlaps(range0, range1) or overlaps(range1, range0):
		numberOfOverlaps += 1

print(f"Answer 1: {numberOfPairs}\nAnswer 2: {numberOfOverlaps}")