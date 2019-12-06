#!/usr/bin/env python3

from collections import defaultdict, deque


FILE_NAME = 'input.txt'


def load_data(filename=FILE_NAME):
    with open(filename) as file:
        return file.read().splitlines()


def process_data(data):
    mapped_planets = defaultdict(list)
    for orbit in data:
        planet, other_planet = orbit.split(')')
        mapped_planets[planet].append(other_planet)
    return mapped_planets


def dist_and_path_source(map, source):
    unvisited = deque([source])
    dist = {source: 0,}
    path = {source : 0, }
    while len(unvisited) != 0:
        planet = unvisited.popleft()
        for other_planet in map[planet]:
            if other_planet not in dist:
                dist[other_planet] = dist[planet] + 1
                path[other_planet] = planet
            unvisited.append(other_planet)
    return dist, path


def reconstruct_path(path, node):
    r_path = []
    curr = node
    while curr != 0:
        curr = path[curr]
        r_path.append(curr)
    return r_path


def find_min_dis(path, a, b):
    connections_a = reconstruct_path(path, a)
    connections_b = reconstruct_path(path, b)
    for i, node in enumerate(connections_a):
        if node in connections_b:
            return i + connections_b.index(node)
        

if __name__ == '__main__':
    data = load_data()
    mapped_planets = process_data(data)
    dist, path = dist_and_path_source(mapped_planets, 'COM')
    print(f"part 1: {sum(dist.values())}")
    print(f"part 2: {find_min_dis(path, 'YOU', 'SAN')}")
