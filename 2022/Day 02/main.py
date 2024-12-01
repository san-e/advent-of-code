with open("input.txt", "r") as f:
	input = [x.replace("\n", "") for x in f.readlines()]
input = [x.split(" ") for x in input]


def outcome(opponent, you, part = 0):
	match opponent:
		case "A":				# Rock
			if you == "X":		# Rock
				return "draw" if not part else "Z"
			elif you == "Y": 	# Paper
				return "win" if not part else "X"
			elif you == "Z":	# Scissiors
				return "loss" if not part else "Y"

		case "B":				# Paper		
			if you == "X":		# Rock
				return "loss" if not part else "X" 
			elif you == "Y": 	# Paper
				return "draw" if not part else "Y" 
			elif you == "Z":	# Scissiors
				return "win" if not part else "Z"

		case "C":				# Scissors
			if you == "X":		# Rock
				return "win" if not part else "Y"
			elif you == "Y": 	# Paper
				return "loss" if not part else "Z"
			elif you == "Z":	# Scissiors
				return "draw" if not part else "X"		


guide = {
	"X" : 1, # Rock
	"Y" : 2, # Paper
	"Z" : 3, # Scissors
}
conditions = {
	"loss" : 0,
	"X" : 0,
	"draw" : 3,
	"Y": 3,
	"win" : 6,
	"Z" : 6
}


scoreP1 = 0
scoreP2 = 0
for opponent, you in input:
	scoreP1 += guide[you] + conditions[outcome(opponent, you)]
	scoreP2 += guide[outcome(opponent, you, part = 1)] + conditions[you]

print(f"Answer 1: {scoreP1}\nAnswer 2: {scoreP2}")