with open("input.txt", "r") as f:
	input = f.read()

input = input.split("\n\n")
input = [[int(i) for i in calories.split("\n")] for calories in input]
input = [sum(elf) for elf in input]
input.sort(reverse=True)

answer = input[0] + input[1] + input[2]

print(f"Answer 1: {input[0]}\nAnswer 2: {answer}")