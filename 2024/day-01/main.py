import sys, os

sys.path.append("..")
os.chdir(sys.path[0])
from aoc_common import get_input, get_test_input, test


def part1(puzzle_input: list):
    left_list = []
    right_list = []
    for i in puzzle_input:
        left_list.append(int(i.split("   ")[0]))
        right_list.append(int(i.split("   ")[-1]))
    left_list.sort()
    right_list.sort()

    distances = 0
    for left, right in zip(left_list, right_list):
        distances += abs(left - right)

    return distances

def part2(puzzle_input: list):
    left_list = []
    right_list = []
    for i in puzzle_input:
        left_list.append(int(i.split("   ")[0]))
        right_list.append(int(i.split("   ")[-1]))
    
    for i in range(len(left_list)):
        number = left_list[i]
        left_list[i] = number * right_list.count(number)

    return sum(left_list)

def main():
    test(1, "test-input-p1.txt", part1)
    test(2, "test-input-p2.txt", part2)

    input = get_input("input.txt")
    print(f"Part 1: {part1(input)}\nPart 2: {part2(input)}")


if __name__ == "__main__":
    main()
