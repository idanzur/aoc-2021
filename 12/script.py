#!/usr/bin/python3
from os import name
from typing import List
from pprint import pprint
from collections import defaultdict


file = './sample.txt' if 0 else './input.txt'


class Cave:
    def __init__(self, name: str) -> None:
        self.name = name
        self.paths = []
        self.lower = name.lower() == name

    def add(self, cave):
        self.paths.append(cave)

    def __repr__(self) -> str:
        return f'{self.name}'


def find_path(visited: List[Cave], paths=set()):
    start = visited[-1]
    if start.name == 'end':
        paths.add(str(visited))
        return
    for cave in start.paths:
        if cave.lower and cave in visited:
            continue
        find_path(visited + [cave], paths)
    return paths


def is_alowed(cave: Cave, visited: List[Cave]):
    if not cave.lower or cave.name == 'end':
        return True
    if cave.name == 'start':
        return False
    names = defaultdict(int)
    for c in visited:
        if c.lower:
            names[c.name] += 1
    if 2 in names.values():
        return cave.name not in names
    return True


def find_path2(visited: List[Cave], paths=set()):
    start = visited[-1]
    if start.name == 'end':
        paths.add(str(visited))
        return
    for cave in start.paths:
        if is_alowed(cave, visited):
            find_path2(visited + [cave], paths)
    return paths


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
    paths = find_path([caves['start']])
    print(f'part1: {len(paths)}')


def part2():
    caves = load_data()
    paths = find_path2([caves['start']])
    print(f'part2: {len(paths)}')


if __name__ == '__main__':
    part2()
