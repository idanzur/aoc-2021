#!/usr/bin/python3
from dataclasses import dataclass
from typing import Tuple, List

file = './sample.txt' if 0 else './input.txt'


@dataclass
class Step:
    switch: bool
    x: Tuple[int, int]
    y: Tuple[int, int]
    z: Tuple[int, int]


def get_range(origanl, bound):
    return max(origanl[0], bound[0]), min(origanl[1], bound[1])+1


def part1():
    with open(file) as f:
        data = f.read()

    steps: List[Step] = []
    for row in data.splitlines():
        switch, ranges = row.split(' ')
        x, y, z = [tuple(map(int, axis[2:].split('..')))
                   for axis in ranges.split(',')]
        switch = switch == 'on'
        steps.append(Step(switch, x, y, z))

    grid = {}
    bounds = (-50, 50)
    for step in steps:
        for x in range(*get_range(step.x, bounds)):
            for y in range(*get_range(step.y, bounds)):
                for z in range(*get_range(step.z, bounds)):
                    grid[(x, y, z)] = step.switch

    res = sum(grid.values())
    print(f'part1: {res}')


def part2():
    pass


if __name__ == '__main__':
    part1()
    # part2()
