import sys, os
sys.path.append('..')
os.chdir(sys.path[0])
from aoc_common import get_input, get_test_input, test

def get_neighbours(input: list, x: int, y: int, fallback: str = '.') -> str:
    up = input[y-1][x] if y > 0 else fallback
    down = input[y+1][x] if y < len(input) - 1 else fallback
    left = input[y][x-1] if x > 0 else fallback
    right = input[y][x+1] if x < len(input[y]) - 1 else fallback
    upleft = input[y-1][x-1] if x > 0 and y > 0 else fallback
    upright = input[y-1][x+1] if x < len(input[y]) - 1 and y > 0 else fallback
    downleft = input[y+1][x-1] if x > 0 and y < len(input) - 1 else fallback
    downright = input[y+1][x+1] if x < len(input[y]) - 1 and y < len(input) - 1 else fallback

    # print(f"{upleft} {up} {upright}")
    # print(f"{left} {input[y][x]} {right}")
    # print(f"{downleft} {down} {downright}")

    return (upleft, (y-1,x-1)), (up, (y-1,x)), (upright,(y-1,x+1)), (right, (y,x+1)), \
        (downright, (y+1, x+1)), (down,(y+1, x)), (downleft, (y+1, x-1)), (left, (y, x-1))

def process_p1(input: list, symbols: set):
    numbers = []
    for y, line in enumerate(input):
        number = ""
        valid = False
        for x, char in enumerate(line):
            if not char.isdigit():
                continue
            neighbours = [n[0] for n in get_neighbours(input, x, y)]
            right = neighbours[3]
            if right.isdigit() or char.isdigit():
                number += char
            if set(neighbours).intersection(symbols):
                valid = True
    
            if valid and number and not right.isdigit():
                numbers.append(int(number))
                # print(f"{number} is valid")
                number = ""
                valid = False
            elif not right.isdigit():
                # print(f"{number} is invalid")
                number = ""
            
    return sum(numbers)

def process_p2(input: str, gear: str = '*'):
    product_sum = 0
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char != gear:
                continue
            numbers = ["1", "1"]
            setnum = {0 : False, 1: False}
            neighbours = get_neighbours(input, x, y)
            iteration = 0
            lock = False
            lasty = -1
            for i, _ in enumerate(neighbours):
                nchar, location = _
                if not nchar.isdigit():
                    lock = False
                    continue
                if location[0] != lasty:
                    lock = False
                lasty = location[0]
                if lock and nchar.isdigit():
                    continue

                iteration += 1
                leftreached, rightreached = False, False
                n = 1
                numbers[iteration - 1] = nchar
                while True:
                    if not leftreached:
                        if location[1] - n < 0 or not input[location[0]][location[1] - n].isdigit():
                            leftreached = True
                            lock = True
                        else:
                            numbers[iteration - 1] = input[location[0]][location[1] - n] + numbers[iteration - 1]
                    if not rightreached:
                        if location[1] + n >= len(input[location[0]]) -1 or not input[location[0]][location[1] + n].isdigit():
                            rightreached = True
                            lock = True
                        else:
                            numbers[iteration - 1] += input[location[0]][location[1] + n]

                    if leftreached and rightreached:
                        setnum[iteration -1] = True
                        break
                    n += 1

                if iteration >= 2:
                    product_sum += int(numbers[0]) * int(numbers[1])
                    break

    return product_sum


def main():
    symbols = {
        '*', '&', '+', '-', '#',
        '@', '=', '%', '$','/'
    }

    test(1, "./test-input-p1.txt", process_p1, symbols)
    test(2, "./test-input-p2.txt", process_p2)

    print(process_p2(get_input("./input.txt")))


if __name__ == '__main__':
    main()