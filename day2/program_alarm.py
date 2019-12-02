#!/usr/bin/env python3


FILE_NAME = 'input.txt'


def load_data(filename=FILE_NAME):
    with open(filename) as file:
        return [int(val) for val in file.read().split(',')]


def process_opcodes(data=None):
    if not data:
        data = load_data()
    
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
        

def restore_state(data=None):
    if not data:
        data = load_data()
    data[1] = 12
    data[2] = 2
    processed = process_opcodes(data)
    return processed[0]


if __name__ == '__main__':
    print(f'part 1 answer: {restore_state()}')






