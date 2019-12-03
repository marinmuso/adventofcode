#!/usr/bin/env python3


FILE_NAME = 'input.txt'


def load_data(filename=FILE_NAME):
    with open(filename) as file:
        coords = file.read().strip().split()
        return [coord.split(',') for coord in coords]


def get_intersections(data): 
    movements = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0),
    }

    visited_points = []
    for row in data:
        curr_x, curr_y = 0, 0
        points = []
        for coord in row:
            direction = coord[0]
            amount = int(coord.strip(direction))
            for _ in range(amount):
                x, y = movements[direction]
                curr_x, curr_y = curr_x + x, curr_y + y
                points.append((curr_x, curr_y))  
        visited_points.append(points)
    return set.intersection(*[set(val) for val in visited_points])


def find_min_distance(data=None, curr_x=0, curr_y=0):
    if not data:
        data = load_data()
    
    intersections = get_intersections(data)
    
    min_distance = float('inf')
    for x, y in intersections:
        distance = abs(curr_x - x) + abs(curr_y - y)
        min_distance = min(min_distance, distance)
    return min_distance


if __name__ == '__main__':
    print(f'part 1: {find_min_distance()}')


    






        
  