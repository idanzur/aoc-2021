#!/usr/bin/python3
from collections import defaultdict

file = './sample.txt' if 0 else './input.txt'


class Enhancer:
    def __init__(self, grid, lookup) -> None:
        self.lookup = lookup
        self.grid = grid
        self.start_x, self.start_y = min(grid)
        self.end_x, self.end_y = max(grid)

    def enhance(self, offset):
        new_grid = defaultdict(lambda: '.')
        for y in range(self.start_y - offset, self.end_y + 1 + offset):
            for x in range(self.start_x - offset, self.end_x + 1 + offset):
                new_grid[(x, y)] = self.lookup[self.calc_val(x, y)]
        self.grid = self.grid | new_grid

    def calc_val(self, x, y):
        res = ''
        for _y in range(y - 1, y + 2):
            for _x in range(x - 1, x + 2):
                res += '1' if self.grid[(_x, _y)] == '#' else '0'
        return int(res, 2)
    
    def count(self, offset):
        s = 0
        for y in range(self.start_y-offset, self.end_y + 1 + offset):
            for x in range(self.start_x-offset, self.end_x + 1 + offset):
                if self.grid[(x,y)] == '#':
                    s += 1
        return s      



def load_data():
    with open(file) as f:
        data = f.read()
    lookup, data = data.split('\n\n')
    grid = defaultdict(lambda: '.')
    for y, row in enumerate(data.splitlines()):
        for x, cell in enumerate(row):
            grid[(x, y)] = cell
    return grid, lookup


def part1():
    grid, lookup = load_data()
    enhancer = Enhancer(grid, lookup)
    loops = 2
    for _ in range(loops):
        enhancer.enhance(loops * 3)
    res = enhancer.count(loops * 2)
    print(f'part1: {res}')

def part2():
    grid, lookup = load_data()
    enhancer = Enhancer(grid, lookup)
    loops = 50
    for _ in range(loops):
        enhancer.enhance(loops * 3)
    res = enhancer.count(loops * 2)
    print(f'part2: {res}')

if __name__  == '__main__':
    part1()
    part2()
