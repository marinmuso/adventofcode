#!/usr/bin/env python3

PUZZLE_RANGE = range(372037, 905157)


def check_never_decreasing(num):
    num = str(num)
    return all(a <= b for a, b in zip(num, num[1:]))
  
    
def check_adj_digits(num):
    num = str(num)
    return any(a == b for a, b in zip(num, num[1:]))


def check_group_digits(num):
    num = str(num)
    return 2 in [num.count(digit) for digit in num]
        

def possible_passwords(part=1, range_nums=PUZZLE_RANGE):
    check = {
        1: check_adj_digits,
        2: check_group_digits
    }
    possible_pws = 0
    for num in range_nums:
        if check_never_decreasing(num) and check[part](num):
            possible_pws += 1 
    return possible_pws


if __name__ == '__main__':
    print(f'Part 1: {possible_passwords(part=1)}')
    print(f'Part 2: {possible_passwords(part=2)}')
