import sys, os

sys.path.append("..")
os.chdir(sys.path[0])
from aoc_common import get_input, get_test_input, test, print_results


def part1(puzzle_input: list):
    reports = [[int(_) for _ in level.split(" ")] for level in puzzle_input]

    safe_reports = 0
    for report in reports:
        increasing = (report[0] - report[1]) < 0
        unsafe = False
        for i in range(1, len(report)):
            if ((report[i - 1] - report[i]) < 0) != increasing:
                unsafe = True
            if not (1 <= abs(report[i - 1] - report[i]) <= 3):
                unsafe = True

        if unsafe == True:
            continue

        safe_reports += 1

    return safe_reports


def part2(puzzle_input: list):
    reports = [[int(_) for _ in level.split(" ")] for level in puzzle_input]

    safe_reports = 0
    for report in reports:
        increasing = (report[0] - report[1]) < 0
        unsafe = False
        tolerance = 1
        for i in range(1, len(report)):
            if ((report[i - 1] - report[i]) < 0) != increasing:
                if tolerance > 0:
                    tolerance -= 1
                    continue
                unsafe = True
            if not (1 <= abs(report[i - 1] - report[i]) <= 3):
                if tolerance > 0:
                    tolerance -= 1
                    continue
                unsafe = True

        if unsafe == True:
            continue

        safe_reports += 1

    return safe_reports


def main():
    #test(1, "test-input-p1.txt", part1)
    print(part2(get_test_input("test-input-p1.txt")[0]))
    #print_results(get_input("input.txt"), part1, part2)


if __name__ == "__main__":
    main()
