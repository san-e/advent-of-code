import sys, os
from pprint import pprint
from collections import defaultdict

sys.path.append("..")
os.chdir(sys.path[0])
from aoc_common import get_input, get_test_input, test


def process_input(input: list):
    order = input[0].split(",")
    input = input[2:]
    input = "\n".join(input)
    input = input.split("\n\n")

    boards = [
        [[z for z in y.strip().split(" ") if z] for y in x.strip().split("\n")]
        for x in input
    ]

    return order, boards


def precompute_indices(boards: list):
    indices = []
    for board in boards:
        indexes = {}
        for x, row in enumerate(board):
            for y, column in enumerate(row):
                indexes[column] = (x, y)
        indices.append(indexes)

    return indices


def is_game_over(marks: list, past_winners: set = set()):
    width, height = (5, 5)
    for board_index, board in enumerate(marks):
        aaaa = [defaultdict(int), defaultdict(int)]
        for mark in board:
            aaaa[0][mark[0]] += 1
            aaaa[1][mark[1]] += 1
            if aaaa[0][mark[0]] == width or aaaa[1][mark[1]] == height:
                return board_index if board_index not in past_winners else -1
    return -1


def part1(input: list):
    order, boards = process_input(input)
    indices = precompute_indices(boards)
    marks = [set() for _ in range(len(boards))]

    for number in order:
        for board_index, _ in enumerate(boards):
            index = indices[board_index].get(number, False)
            if index == False:
                continue
            marks[board_index].add(index)
        winner_index = is_game_over(marks)  # -1 if no board has won yet
        last_number = int(number)
        if winner_index > -1:
            break

    winning_board = boards[winner_index]
    unmarked_numbers = 0
    for x, row in enumerate(winning_board):
        for y, number in enumerate(row):
            if (x, y) not in marks[winner_index]:
                unmarked_numbers += int(number)
    return unmarked_numbers * last_number


def part2(input: list):
    order, boards = process_input(input)
    indices = precompute_indices(boards)
    marks = [set() for _ in range(len(boards))]
    past_winners = set()
    current_winner = -1
    for number in order:
        for board_index, _ in enumerate(boards):
            index = indices[board_index].get(number, False)
            if index == False:
                continue
            marks[board_index].add(index)
        winner_index = is_game_over(marks, past_winners)  # -1 if no board has won yet
        last_number = int(number)
        if winner_index > -1:
            past_winners.add(winner_index)
            current_winner = winner_index
            current_last_number = last_number
    print(current_winner)
    winning_board = boards[current_winner]
    unmarked_numbers = 0
    for x, row in enumerate(winning_board):
        for y, number in enumerate(row):
            if (x, y) not in marks[current_winner]:
                unmarked_numbers += int(number)
    return unmarked_numbers * last_number


def main():
    test(1, "test-input-p1.txt", part1)
    print(f"Part 1: {part1(get_input('input.txt'))}")
    print(f"Part 2: {part2(get_test_input('test-input-p1.txt')[0])}")


if __name__ == "__main__":
    main()
