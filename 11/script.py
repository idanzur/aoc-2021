#!/usr/bin/python3
from dataclasses import dataclass
from typing import List, Tuple

file = './sample.txt' if 0 else './input.txt'

CROSSED_FORMAT = '\033[1m{}\033[0m'

@dataclass
class Cell:
    val: int
    flashed: bool = False
    def __repr__(self) -> str:
        if self.flashed:
            return CROSSED_FORMAT.format(self.val)
        return str(self.val)

class Grid:
    SIZE = 10
    def __init__(self, cells: List[List[Cell]]):
        self.cells = cells
        self.flashes = 0

    def step(self):
        for row in self.cells:
            for cell in row:
                cell.val += 1

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
                        self.flashes += 1
        self.clean()

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
        res = ""
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
            t.append(Cell(val=int(n)))
        cells.append(t)
    
    return Grid(cells)

def part1():
    grid = load_data()
    for _ in range(100):
        grid.step()
    print(f'part1: {grid.flashes}')

def part2():
    grid = load_data()
    i = 0
    while True:
        i += 1
        grid.step()
        all_zero = True
        for row in grid.cells:
            for cell in row:
                if cell.val != 0:
                    all_zero = False
                    break
        if all_zero:
            break   
        
    print(f'part2: {i}')

if __name__  == '__main__':
    part1()
    part2()
