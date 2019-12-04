#!/usr/bin/env python3

PUZZLE_RANGE = range(372037, 905157)


def check_adj_digits(num):
    num = str(num)
    return any(a == b for a, b in zip(num, num[1:]))


def check_never_decreasing(num):
    num = str(num)
    return all(a <= b for a, b in zip(num, num[1:]))


def possible_password(range_nums=PUZZLE_RANGE):
    possible_pws = 0
    for num in range_nums:
        if check_adj_digits(num) and check_never_decreasing(num):
            possible_pws += 1
    return possible_pws


if __name__ == '__main__':
    print(f'Part 1: {possible_password()}')
