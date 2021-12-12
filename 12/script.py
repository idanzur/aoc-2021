#!/usr/bin/python3
from typing import List


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


def find_path2(visited: List[Cave], paths=set(), twice: bool = False):
    start = visited[-1]
    if start.name == 'end':
        paths.add(str(visited))
        return
    for cave in start.paths:
        if cave.name == 'start':
            continue
        if cave.lower:
            if twice:
                if cave not in visited:
                    find_path2(visited + [cave], paths, twice)
            else:
                find_path2(visited + [cave], paths, cave in visited)
        else:
            find_path2(visited + [cave], paths, twice)
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
