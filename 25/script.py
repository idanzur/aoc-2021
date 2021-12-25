#!/usr/bin/python3
from typing import List, Tuple


file = './sample.txt' if 0 else './input.txt'


class Grid:
    def __init__(self, grid: List[List[str]]) -> None:
        self.grid = grid
        self.changed = False
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def step(self):
        self.changed = False
        self.move('>', (1, 0))
        self.move('v', (0, 1))
        return self.changed

    def move(self, val: str, dir: Tuple[int, int]):
        visited = set()
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if (x, y) in visited:
                    continue
                if cell != '.':
                    visited.add((x, y))
                if cell == val:
                    new_y = (y+dir[1]) % self.height
                    new_x = (x+dir[0]) % self.width
                    if (new_x, new_y) not in visited and self.grid[new_y][new_x] == '.':
                        self.grid[new_y][new_x] = val
                        self.grid[y][x] = '.'
                        self.changed = True
                        visited.add((new_x, new_y))

    def __repr__(self):
        return '\n'.join([''.join(row) for row in self.grid])


def part1():
    with open(file) as f:
        data = f.read()

    grid = [[cell for cell in row] for row in data.splitlines()]
    grid = Grid(grid)
    i = 1
    while grid.step():
        i += 1
    print(f'part1: {i}')


def part2():
    pass


if __name__ == '__main__':
    part1()
    # part2()
