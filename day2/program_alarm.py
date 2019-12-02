#!/usr/bin/env python3

from itertools import product


FILE_NAME = 'input.txt'


def load_data(filename=FILE_NAME):
    with open(filename) as file:
        return [int(val) for val in file.read().split(',')]


def process_opcodes(data):
    ops = {
        1: lambda x, y: x + y,
        2: lambda x, y: x * y,
    }
    i = 0
    while i < len(data) - 4:
        op = data[i]
        if op == 99:
            break
        first_num, second_num, res = data[i+1], data[i+2], data[i+3]
        data[res] = ops[op](data[first_num], data[second_num])
        i += 4
    return data
        

def restore_state(noun, verb, data=None):
    if not data:
        data = load_data()
    data[1] = noun
    data[2] = verb
    processed = process_opcodes(data)
    return processed[0]


def crack_output(desired_output):
    for noun, verb in product(range(100), repeat=2):
        if restore_state(noun, verb) == desired_output:
            return noun, verb


if __name__ == '__main__':
    print(f'part 1: {restore_state(12, 1)}')
    print(f'part 2: {crack_output(19690720)}')
