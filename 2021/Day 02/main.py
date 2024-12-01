import sys, os

sys.path.append("..")
os.chdir(sys.path[0])
from aoc_common import get_input, get_test_input, test


def part1(input: list):
    position = [0, 0]
    for instruction in input:
        instruction = instruction.split(" ")
        direction = instruction[0]
        amount = int(instruction[1])

        if direction == "forward":
            position[0] += amount
        elif direction == "up":
            position[1] += amount
        elif direction == "down":
            position[1] -= amount
    return position[0] * -position[1]


def part2(input: list):
    aim = 0
    position = [0, 0]
    for instruction in input:
        instruction = instruction.split(" ")
        direction = instruction[0]
        amount = int(instruction[1])

        if direction == "forward":
            position[0] += amount
            position[1] += aim * amount
        elif direction == "up":
            aim -= amount
        elif direction == "down":
            aim += amount

    return position[0] * position[1]


def main():
    test(1, "test-input-p1.txt", part1)
    test(2, "test-input-p2.txt", part2)

    print(f"Part 1: {part1(get_input('input.txt'))}")
    print(f"Part 2: {part2(get_input('input.txt'))}")


if __name__ == "__main__":
    main()
