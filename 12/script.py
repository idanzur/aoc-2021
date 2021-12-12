#!/usr/bin/python3
from os import name, path
from typing import List
from dataclasses import dataclass
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
def find_path(start: Cave, visited: List[Cave]):
    global paths
    if start.name == 'end':
        paths.append(visited + [start])
    for cave in start.paths:
        if cave.name.lower() == cave.name and cave in visited:
            continue
        find_path(cave, visited + [start])
        
def part1():
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
    
    find_path(caves['start'], [])
    print(f'part1: {len(paths)}')

def part2():
    pass

if __name__  == '__main__':
    part1()
