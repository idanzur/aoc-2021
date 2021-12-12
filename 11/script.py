#!/usr/bin/python3
from dataclasses import dataclass
from typing import List
import numpy as np

file = './sample.txt' if 0 else './input.txt'

FLASHED_FORMAT = '\033[1m{}\033[0m'

@dataclass
class Cell:
    val: int
    flashed: bool = False
    def __repr__(self) -> str:
        if self.flashed:
            return FLASHED_FORMAT.format(self.val)
        return str(self.val)

class Grid:
    SIZE = 10
    def __init__(self, cells: List[List[Cell]]):
        self.cells = cells

    def step(self, clean=True):
        for row in self.cells:
            for cell in row:
                cell.val += 1
        flashes = 0
        change = True
        while change:
            change = False
            for y, row in enumerate(self.cells):
                for x, cell in enumerate(row):
                    if cell.val > 9:
                        change = True
                        self.flash(x, y)
                        cell.flashed = True
                        cell.val = 0
                        flashes += 1
        if clean:
            self.clean()
        return flashes

    def clean(self):
        for row in self.cells:
            for cell in row:
                cell.flashed = False   

    def flash(self, x, y):        
        for _x in range(x - 1, x + 2):
            for _y in range(y - 1, y + 2):
                if 0 <= _x < self.SIZE and 0 <= _y < self.SIZE and (_x != x or _y != y):
                    cell = self.cells[_y][_x]
                    if not cell.flashed:
                        cell.val += 1

    def __repr__(self) -> str:
        res = ''
        for row in self.cells:
            for cell in row:
                res += str(cell)
            res += '\n'
        return res

def load_data() -> Grid:
    with open(file) as f:
        data = f.read()
    cells = []
    for row in data.splitlines():
        t = []
        for n in row:
            t.append(Cell(int(n)))
        cells.append(t)
    cells = np.array(cells)
    return Grid(cells)

def part1():
    grid = load_data()
    flashes = sum([grid.step() for _ in range(100)])
    print(f'part1: {flashes}')

def part2():
    grid = load_data()
    i = 1
    while grid.step() != grid.SIZE ** 2:
        i += 1        
    print(f'part2: {i}')

if __name__  == '__main__':
    part1()
    part2()
