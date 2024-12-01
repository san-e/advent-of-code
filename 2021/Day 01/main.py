import sys, os

sys.path.append("..")
os.chdir(sys.path[0])
from aoc_common import get_input, get_test_input, test


def part1(input: list):
    input = [int(x) for x in input]
    tally = 0
    previous_number = input[0]
    for number in input:
        if number > previous_number:
            tally += 1
        previous_number = number

    return tally


def part2(input: list):
    input = [int(x) for x in input]
    tally = 0
    previous_window = input[0] + input[1] + input[2]
    for window_center in range(2, len(input)):
        if (
            len(input) - window_center == 1
        ):  # accounting for off-by-one difference between index and length here
            break
        current_window = (
            input[window_center - 1] + input[window_center] + input[window_center + 1]
        )
        if current_window > previous_window:
            tally += 1
        previous_window = current_window
    return tally


def main():
    test(1, "test-input-p1.txt", part1)
    test(2, "test-input-p2.txt", part2)

    print(f"Part 1: {part1(get_input('input.txt'))}")
    print(f"Part 2: {part2(get_input('input.txt'))}")


if __name__ == "__main__":
    main()
