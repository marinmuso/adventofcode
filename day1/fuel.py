#!/usr/bin/env python3


FILE = 'input.txt'


def load_data(filename=FILE):
    with open(filename) as file:
        data = file.readlines()
    return [int(mass) for mass in data]


def calculate_fuel(data=None):
    if not data:
        data = load_data()
    total = sum(mass // 3 - 2 for mass in data)
    return total


def additional_fuel(data=None):
    if not data:
        data = load_data()
    total = 0
    for mass in data:
        while mass > 0:
            mass = mass // 3 - 2
            if mass > 0:
                total += mass
    return total


if __name__ == '__main__':
    required = calculate_fuel()
    additional = additional_fuel()
    print(f'part 1: {required}, part 2: {additional}')
