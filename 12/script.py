#!/usr/bin/python3
from typing import List
from pprint import pprint


file = './sample.txt' if 0 else './input.txt'

class Cave:
    def __init__(self, name: str) -> None:
        self.name = name
        self.paths = []

    def add(self, cave):
        self.paths.append(cave)

    def __repr__(self) -> str:
        return f'{self.name}'

paths = []
def find_path(start: Cave, visited: List[Cave], allowed_twice: Cave = None):
    global paths
    if start.name == 'end':
        new_path = visited + [start]
        if new_path not in paths:
            paths.append(new_path)
    for cave in start.paths:
        if cave.name.lower() == cave.name:
            if cave is allowed_twice and visited.count(cave) < 2:
                pass
            elif cave in visited:
                continue
        find_path(cave, visited + [start], allowed_twice)

def load_data():
    with open(file) as f:
        data = f.read()
    caves = {}
    for row in data.splitlines():
        name_a, name_b = row.split('-')
        cave_a = caves.get(name_a, Cave(name_a))
        cave_b = caves.get(name_b, Cave(name_b))
        cave_a.add(cave_b)
        cave_b.add(cave_a)
        caves[name_a] = cave_a
        caves[name_b] = cave_b
    return caves

def part1():
    caves = load_data()
    find_path(caves['start'], [])
    print(f'part1: {len(paths)}')

def part2():
    caves = load_data()
    for name, cave in caves.items():
        if name.lower() == name and name not in ['start', 'end']:
            find_path(caves['start'], [], cave)
    print(f'part2: {len(paths)}')

if __name__  == '__main__':
    part2()
