import string
with open("input.txt", "r") as f:
	input = f.readlines()
		#compartment 1	   #compartment 2
part1 = [[i[0:len(i)//2], i[len(i)//2:].rstrip("\n")] for i in input]	# seperate backpacks into compartments
part2 = [[input[i].rstrip("\n"), input[i+1].rstrip("\n"), input[i+2].rstrip("\n")] for i in list(range(len(input)))[::3]]	# merge every 3 backpacks into one group


priorities = {letter: index + 1 for index, letter in enumerate(string.ascii_letters)}

values0 = []
for compartment1, compartment2 in part1:
	compartment1 = set(compartment1)
	compartment2 = set(compartment2)

	for letter in compartment1:
		if letter in compartment2:
			values0.append(priorities[letter])

values1 = []
for elf0, elf1, elf2 in part2:
	elf0 = set(elf0)
	efl1 = set(elf1)
	elf2 = set(elf2)

	for letter in elf0:
		if letter in elf1 and letter in elf2:
			values1.append(priorities[letter])

print(f"Answer 1: {sum(values0)}\nAnswer 2: {sum(values1)}")