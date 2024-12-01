import sys, os
sys.path.append('..')
os.chdir(sys.path[0])
from aoc_common import get_input, get_test_input, test

def parse(input: str, part: int = 0):
    time = [x for x in input[0].split(" ") if x][1:]
    distance = [x for x in input[1].split(" ") if x][1:]
    if part == 0:
        return {int(x): int(y) for x, y in zip(time, distance)}
    else:
        return {int("".join(time)): int("".join(distance))}

def calculate_distance(held, remaining):
    return remaining * held

def process_p1(input: dict, part: int = 0):
    input = parse(input, part)
    games = {}
    total = 0
    for i, x in enumerate(input.items()):
        time, distance = x
        games[i] = []
        for hold_time in range(1, time):
            distance_travelled = calculate_distance(hold_time, time - hold_time)
            if distance_travelled > distance:
                if part == 0:
                    games[i].append(distance_travelled)
                else:
                    total += 1

    if part == 0:
        total = 1
        for game in games.values():
            total *= len(game)

    return total

def process_p2(input: str):
    return process_p1(input, 1)

def main():
    test(1, "./test-input-p1.txt", process_p1)
    test(2, "./test-input-p2.txt", process_p2)

    input = get_input("./input.txt")
    answer1 = process_p1(input)
    print(f"Part 1: {answer1}")
    answer2 = process_p2(input)
    print(f"Part 2: {answer2}")    
    

if __name__ == '__main__':
    main()