with open("input.txt") as f:
	input = f.read().split("\n")

delays = {
	"addx": 2,
	"noop": 1,
}
registerX = 1
spritePosition = [registerX - 1, registerX, registerX + 1]
cycle = 0
screenColumn = 0
screenRow = 0
signals = {}
screen = [["" for _ in range(40)] for _ in range(6)]
for instruction in input:
	instruction = instruction.split(" ")
	match instruction[0]:
		case "addx":
			instruction, value = instruction
			for _ in range(delays["addx"]):
				if screenColumn % 40 == 0 and screenColumn:
					screenColumn = 0
					if screenRow < 5: screenRow += 1

				if screenColumn in spritePosition:
					screen[screenRow][screenColumn] = "#"
				else:
					screen[screenRow][screenColumn] = " "
				cycle += 1
				screenColumn += 1
				if cycle % 20 == 0: signals[cycle] = (cycle * registerX)
			registerX += int(value)
			spritePosition = [registerX - 1, registerX, registerX + 1]
		
		case "noop":
			for _ in range(delays["noop"]):
				if screenColumn % 40 == 0 and screenColumn:
					screenColumn = 0
					if screenRow < 5: screenRow += 1

				if screenColumn in spritePosition:
					screen[screenRow][screenColumn] = "#"
				else:
					screen[screenRow][screenColumn] = " "
				cycle += 1
				screenColumn += 1
				if cycle % 20 == 0: signals[cycle] = (cycle * registerX)


sumOfSignalStrenght = signals[20] + signals[60] + signals[100] + signals[140] + signals[180] + signals[220]
print(f"Answer 1: {sumOfSignalStrenght}\nAnswer 2 (requires some manual deciphering):")
for row in screen:
	for column in row:
		print(column, end="")
	print("")