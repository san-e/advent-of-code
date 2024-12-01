import sys, os
sys.path.append("..")
os.chdir(sys.path[0])
from aoc_common import get_input, get_test_input, test
import math
from collections import defaultdict

def parse(input: str):
    out = {}
    for game in input:
        game_info = game.split(":")
        game_id = int(game_info[0].replace("Game ", ""))
        sets = game_info[1].strip().split(";")
        throws = [x.strip().split(", ") for x in sets]
        out[game_id] =  [[y.split(" ") for y in x] for x in throws]
        
    return out

def process_p1(input: str, colors: dict):
    games = parse(input)
    possible_ids = set()

    for id, game in games.items():
        possible = True
        for throw in game:
            for amount, color in throw:
                if int(amount) > colors[color]:
                    possible = False
        
        if possible:
            possible_ids.add(id)

    return sum(possible_ids)

def process_p2(input: str):
    games = parse(input)
    products = []
    for id, game in games.items():
        mongoose = defaultdict(list)
        for throw in game:
            for amount, color in throw:
                mongoose[color].append(int(amount))
        
        products.append(math.prod([max([x for x in amount]) for amount in mongoose.values()]))

    return sum(products)

def main():
    limits = {"red": 12, "green": 13, "blue": 14}

    test(1, "./test-input-p1.txt", process_p1, limits)
    test(2, "./test-input-p2.txt", process_p2)


    input = get_input("input.txt")
    answer1 = process_p1(input, limits)
    answer2 = process_p2(input)

    print(f"Part 1: {answer1}\nPart 2: {answer2}")


if __name__ == "__main__":
    main()