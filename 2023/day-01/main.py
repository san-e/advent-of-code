import sys, os
sys.path.append("..")
os.chdir(sys.path[0])
from aoc_common import get_input, get_test_input, test

def process_p1(input: str) -> int:
    digits = ["".join([char for char in line if char.isnumeric()]) for line in input]
    digits = [int("".join([digit[0], digit[-1]])) for digit in digits]

    return sum(digits)

def process_p2(input: str):
    digit_map = {
        "one": "o1ne",
        "two": "tw2o",
        "three": "thr3ee",
        "four": "fo4ur",
        "five": "fi5ve",
        "six": "s6ix",
        "seven": "sev7en",
        "eight": "eig8ht",
        "nine": "ni9ne"
    }
    new_input = []

    for line in input:
        temp = line
        for d_name, d_replacement in digit_map.items():
            temp = temp.replace(d_name, d_replacement)
            
        new_input.append(temp)

    return process_p1(new_input)

def main():
    test(1, "./test-input-p1.txt", process_p1)
    test(2, "./test-input-p2.txt", process_p2)

    input = get_input("./input.txt")
    answer1 = process_p1(input)
    answer2 = process_p2(input)

    print(f"Answer 1: {answer1}\nAnswer 2: {answer2}")

if __name__ == "__main__":
    main()