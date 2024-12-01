import sys, os
sys.path.append('..')
os.chdir(sys.path[0])
from aoc_common import get_input, get_test_input, test
from collections import defaultdict
from pprint import pprint

def parser(input: str):
    games = {}
    for game in input:
        id = game.split(":")[0].split(" ")[-1]
        numbers = game.split(":")[-1].split("|")
        winning_numbers = numbers[0].strip().split(" ")
        drawn_numbers = numbers[1].strip().split(" ")
        games[int(id)] = {
            "winning_numbers": {x for x in winning_numbers if x},
            "drawn_numbers": [x for x in drawn_numbers if x]
            }

    return games



def process_p1(input: str):
    values = {}
    for id, numbers in parser(input).items():
        winning_numbers = numbers["winning_numbers"]
        drawn_numbers = numbers["drawn_numbers"]

        i = 0
        for number in drawn_numbers:
            if not number in winning_numbers:
                continue
            if i == 0:
                values[id] = 1
            else:
                values[id] = values[id] * 2
            i += 1
    return sum(values.values())

def process_p2(input: str):
    instances = defaultdict(lambda: 1)
    for id , numbers in parser(input).items():
        for _ in range(instances[id]):
            winning_numbers = numbers["winning_numbers"]
            drawn_numbers = numbers["drawn_numbers"]

            matches = 0
            for number in drawn_numbers:
                if number in winning_numbers:
                    matches += 1
            
            for index in range(id + 1, id + matches + 1):
                instances[index] += 1

    return sum(instances.values())

def main():
    test(1, "./test-input-p1.txt", process_p1)
    test(2, "./test-input-p2.txt", process_p2)

    input = get_input("./input.txt")
    answer1 = process_p1(input)
    answer2 = process_p2(input)

    print(f"Part 1: {answer1}\nPart 2: {answer2}")


if __name__ == '__main__':
    main()