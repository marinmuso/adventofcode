#!/usr/bin/env python3

from collections import defaultdict, deque


FILE_NAME = 'input.txt'


def load_data(filename=FILE_NAME):
    with open(filename) as file:
        return file.read().splitlines()


def process_data(data):
    map = defaultdict(list)
    for orbit in data:
        k, v = orbit.split(')')
        map[k].append(v)
    return map


def sum_dis_from_source(map, source):
    unvisited = deque([source])
    dist = {source: 0,}
    while len(unvisited) != 0:
        planet = unvisited.popleft()
        for other_planet in map[planet]:
            if other_planet not in dist:
                dist[other_planet] = dist[planet] + 1
            unvisited.append(other_planet)
    return sum(dist.values())


if __name__ == '__main__':
    data = load_data()
    map = process_data(data)
    print(f"part 1: {sum_dis_from_source(map, 'COM')}")

