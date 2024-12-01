import sys, os

sys.path.append("..")
os.chdir(sys.path[0])
from aoc_common import get_input, get_test_input, test


def part1(input: list):
    zeroes, ones, gamma_rate, epsilon_rate = (0, 0, 0b0, 0b0)
    shift_template = 2 ** (len(input[0]) - 1)

    for column in range(len(input[0])):
        for row in input:
            number = row[column]
            if number == "0":
                zeroes += 1
            else:
                ones += 1

        if ones > zeroes:
            gamma_rate = gamma_rate | (shift_template >> column)
        else:
            epsilon_rate = epsilon_rate ^ (shift_template >> column)

        zeroes, ones = (0, 0)

    return gamma_rate * epsilon_rate


def part2(input: list):
    (
        zeroes,
        ones,
    ) = (0, 0)
    in2 = input
    ratings = [0, 0]
    number_length = len(input[0])
    for rating in range(2):
        for column in range(number_length):
            for row in input:
                number = row[column]
                if number == "0":
                    zeroes += 1
                else:
                    ones += 1

            most_common = int(ones >= zeroes)
            least_common = int(not most_common)
            if rating == 0:
                input = [line for line in input if line[column] == str(most_common)]
            else:
                input = [line for line in input if line[column] == str(least_common)]
            if len(input) == 1:
                ratings[rating] = int(input[0], 2)
                break
            zeroes, ones = (0, 0)
        input = in2

    return ratings[0] * ratings[1]


def main():
    test(1, "test-input-p1.txt", part1)
    test(2, "test-input-p2.txt", part2)

    input = get_input("input.txt")
    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()
