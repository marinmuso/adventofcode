#!/usr/bin/env python3

FILE_NAME = 'input.txt'


def load_data(filename=FILE_NAME):
    with open(filename) as file:
        return [int(val) for val in file.read().split(',')]


def decode_instruction(instruction):
    instruction = str(instruction).zfill(5)
    decoded = {}
    decoded.update([
        ('op', int(instruction[-2:])),
        ('param_one', int(instruction[2])),
        ('param_two', int(instruction[1])),
        ('param_three', int(instruction[0])),
        ])
    return decoded


def process(data, start_num):
    i = 0
    while i < len(data):
        instruction = data[i]

        decoded = decode_instruction(instruction)

        op = decoded['op']

        if op == 99:
            break

        elif op == 3:
            position = data[i+1]
            data[position] = start_num
            i += 2

        elif op == 4:
            position = data[i+1]
            print(data[position])
            i += 2

        else:
            #immediate mode by default
            first_num, second_num, res = data[i+1], data[i+2], data[i+3]
            
            if decoded['param_one'] == 0:
                first_num = data[first_num]

            if decoded['param_two'] == 0:
                second_num = data[second_num]

            if op == 5:
                if first_num != 0:
                    i = second_num
                else:
                    i += 3

            elif op == 6:
                if first_num == 0:
                    i = second_num
                else:
                    i += 3

            elif op == 7:
                if first_num < second_num:
                    data[res] = 1
                else:
                    data[res] = 0
                i += 4

            elif op == 8:
                if first_num == second_num:
                    data[res] = 1
                else:
                    data[res] = 0
                i += 4

            else:
                arithmetic_ops = {1: lambda x, y: x + y, 2: lambda x, y: x * y,}
                data[res] = arithmetic_ops.get(op)(first_num, second_num)
                i += 4


def start():
    print('Enter starting number: ')
    return int(input())


if __name__ == '__main__':
    data = load_data()
    start = start()
    process(data, start)
    